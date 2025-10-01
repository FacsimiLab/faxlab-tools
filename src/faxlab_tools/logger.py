import os
import sys
"""
Logger and tracing utilities for FacsimiLab tools.

This module provides functions to initialize OpenTelemetry tracing and configure logging
for files, Jupyter notebooks, and OpenTelemetry backends. It supports colored notebook output,
log file management, and integration with OpenTelemetry exporters.

Functions:
  - init_tracing: Initialize OpenTelemetry tracing for the process.
  - log_control_center: Configure logging for files, Jupyter notebooks, and OpenTelemetry backends.
"""
import atexit
import logging
from IPython.display import display, Markdown
from rich import print as rprint


from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry._logs import get_logger_provider, set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Module-global guard for tracing initialization
_tracing_initialized = False
_otel_logger_initialized = False

def init_tracing(
  otel_resource: Resource,
  otel_insecure: bool = True,
) -> None:
  """
  Initialize the global OpenTelemetry TracerProvider with the given resource.

  Sets up the tracer provider only once per process. Subsequent calls have no effect.
  The tracer provider is configured to export spans to the OTLP endpoint.

  Args:
    otel_resource (Resource): The OpenTelemetry resource describing the service.
    otel_insecure (bool): Whether to use insecure connection for the OTLP exporter.

  Returns:
    None
  """
  global _tracing_initialized
  if not _tracing_initialized:
    exporter = OTLPSpanExporter(insecure=otel_insecure)
    provider = TracerProvider(resource=otel_resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    _tracing_initialized = True

def log_control_center(
  log_path: str,
  logname: str,
  *,
  file_loglevel: str = "INFO",
  notebook_loglevel: str = "DEBUG",
  otel_resource: Resource = None,
  otel_insecure: bool = True,
) -> tuple[logging.Logger, trace.Tracer]:
  """
  Configure logging and tracing for FacsimiLab tools.

  Sets up logging to a file, Jupyter notebook output (with Markdown), and OpenTelemetry backend.
  Initializes tracing and logger providers if needed.

  Args:
    log_path (str): Path to the log file.
    logname (str): Name for the logger.
    file_loglevel (str): Log level for the file handler.
    notebook_loglevel (str): Log level for notebook output.
    otel_resource (Resource, optional): OpenTelemetry resource for tracing/logging.
    otel_insecure (bool): Whether to use insecure connection for OTLP exporters.

  Returns:
    tuple[logging.Logger, trace.Tracer]: The configured logger and tracer objects.
  """
  global _tracing_initialized
  global _otel_logger_initialized

  existing_tracer = _tracing_initialized
  existing_logger = _otel_logger_initialized

  

  # Initialize tracing if needed
  if not _tracing_initialized:
    if otel_resource is None:
      otel_resource = Resource.create({"service.name": "default-service"})
      rprint("[bold yellow]Warning:[/bold yellow] No resource passed; using default.")
    init_tracing(otel_resource, otel_insecure)

  tracer = trace.get_tracer(__name__)

  # Prepare Python logger
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

  # Set default OTLP endpoint if missing
  if os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT") is None:
    os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "localhost:4317"
    rprint(
      "[bold yellow]Warning:[/bold yellow] OTEL_EXPORTER_OTLP_ENDPOINT not set. Defaulting to `localhost:4317`"
    )

  # Initialize LoggerProvider once
  if not _otel_logger_initialized:
    otel_logger_provider = LoggerProvider(resource=otel_resource)
    set_logger_provider(otel_logger_provider)

    exporter = OTLPLogExporter(insecure=otel_insecure)
    otel_logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    atexit.register(otel_logger_provider.shutdown)

    _otel_logger_initialized = True
  else:
    # Reuse existing logger provider
    otel_logger_provider = get_logger_provider()

  # OpenTelemetry logging handler
  otelHandler = LoggingHandler(level=logging.NOTSET, logger_provider=otel_logger_provider)

  # Formatters
  notebook_fmt = logging.Formatter("%(message)s")
  file_fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
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

  # Initialization log inside a span
  with tracer.start_as_current_span("initialize-logger") as span:
    logger.debug(
      f"Initialized master FacsimiLab Logger. File level: {int_file_level}, Notebook level: {int_notebook_level}, "
      f"OpenTelemetry Exporter: {os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT')}"
    )
    span.set_attribute("log_control_center.existing_tracer", existing_tracer)
    span.set_attribute("log_control_center.existing_logger", existing_logger)

  return logger, tracer
