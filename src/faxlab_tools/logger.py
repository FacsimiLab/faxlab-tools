import os
import sys
import atexit
import logging
from IPython.display import display, Markdown
from rich import print as rprint


from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# Module-global guard for tracing initialization
_tracing_initialized = False


def init_tracing(otel_resource: Resource):
  """
  Initialize the global TracerProvider once with the given resource.
  Subsequent calls do nothing.
  """
  global _tracing_initialized
  if not _tracing_initialized:
    provider = TracerProvider(resource=otel_resource)
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(provider)
    _tracing_initialized = True


def log_control_center(
  log_path: str,
  logname: str,
  *,
  file_loglevel="INFO",
  notebook_loglevel="DEBUG",
  otel_resource: Resource = None,
):
  """
  Configure logging to file, notebook, and OpenTelemetry.
  Automatically initializes tracing if not done yet.
  """
  global _tracing_initialized

  # Initialize tracing if needed
  if not _tracing_initialized:
    if otel_resource is None:
      otel_resource = Resource.create({"service.name": "default-service"})
      rprint("[bold yellow]Warning:[/bold yellow] No resource passed; using default.")
    init_tracing(otel_resource)

  tracer = trace.get_tracer(__name__)

  # Prepare logger
  logger = logging.getLogger(logname)
  for handler in list(logger.handlers):
    logger.removeHandler(handler)
    handler.close()

  # Log levels
  LOG_LEVEL_NUM = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}
  int_file_level = LOG_LEVEL_NUM.get(file_loglevel.upper(), 20)
  int_notebook_level = LOG_LEVEL_NUM.get(notebook_loglevel.upper(), 10)

  # Ensure log file directory exists
  os.makedirs(os.path.dirname(log_path), exist_ok=True)
  open(log_path, "a").close()

  # Notebook handler
  LOG_COLORS = {"WARNING": "yellow", "ERROR": "orange", "CRITICAL": "red"}

  class JupyterStreamHandler(logging.StreamHandler):
    def emit(self, record):
      log_entry = self.format(record)
      levelname = record.levelname
      color_format = f"color: {LOG_COLORS[levelname]}" if levelname in LOG_COLORS else ""
      display(
        Markdown(f"<span style='font-weight:bold; {color_format}'>{levelname}</span> - {log_entry}")
      )

  # OpenTelemetry logging
  otel_logger_provider = LoggerProvider(resource=otel_resource)
  set_logger_provider(otel_logger_provider)

  if os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT") is None:
    os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "localhost:4317"
    rprint(
      "[bold yellow]Warning:[/bold yellow] OTEL_EXPORTER_OTLP_ENDPOINT not set. Defaulting to `localhost:4317`"
    )

  exporter = OTLPLogExporter()
  otel_logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
  atexit.register(otel_logger_provider.shutdown)
  otelHandler = LoggingHandler(level=logging.NOTSET, otel_logger_provider=otel_logger_provider)

  # Formatters
  notebook_fmt = logging.Formatter("%(message)s")
  file_fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%dT%H:%M:%S"
  )

  # Handlers
  stdoutHandler = JupyterStreamHandler(stream=sys.stdout)
  stdoutHandler.setLevel(int_notebook_level)
  stdoutHandler.setFormatter(notebook_fmt)

  fileHandler = logging.FileHandler(log_path)
  fileHandler.setLevel(int_file_level)
  fileHandler.setFormatter(file_fmt)

  # Attach handlers
  logger.addHandler(stdoutHandler)
  logger.addHandler(fileHandler)
  logger.addHandler(otelHandler)

  logger.propagate = False
  logger.setLevel(min(int_file_level, int_notebook_level))

  logger.debug(
    f"Initialized master FacsimiLab Logger. File level: {int_file_level}, Notebook level: {int_notebook_level}, "
    f"OpenTelemetry Exporter: {os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT')}"
  )

  return logger, tracer
