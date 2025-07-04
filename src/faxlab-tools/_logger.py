import logging
import os
from zoneinfo import ZoneInfo
from datetime import datetime


# In [ ]: Python logging
# ------------------------------------------------------------------------


def file_nb_logging(
  log_path, logname, file_loglevel="INFO", notebook_loglevel="DEBUG", stream_loglevel="DEBUG"
):
  import logging
  import sys
  from IPython.display import display, Markdown

  local_tz = ZoneInfo("localtime")

  # Create a new logger or open an existing logger with the notebook name
  logger = logging.getLogger(logname)

  ## Cleanup any existing handlers
  for handler in list(logger.handlers):
    logger.removeHandler(handler)
    handler.close()

  file_loglevel = file_loglevel.upper()
  notebook_loglevel = notebook_loglevel.upper()
  stream_loglevel = stream_loglevel.upper()

  LOG_LEVEL_NUM = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
  }

  # Define HTML colors for log levels
  LOG_COLORS = {
    "WARNING": "yellow",
    "ERROR": "orange",
    "CRITICAL": "red",
  }

  int_notebook_level = LOG_LEVEL_NUM.get(notebook_loglevel, 0)
  int_file_level = LOG_LEVEL_NUM.get(file_loglevel, 0)
  int_stream_level = LOG_LEVEL_NUM.get(stream_loglevel, 0)

  # Prepare the log output destinations
  # --------------------------------------

  # File logger

  # Create the log directory and file if it does not exist yet.
  if os.path.exists(log_path):
    pass
  else:
    try:
      os.makedirs(os.path.join(*log_path.split("/")[:-1]), exist_ok=True)
    except Exception as e:
      print(f"Error creating log directory: {e}")
      pass

    with open(log_path, "w") as file:
      file.write(" ")

  # Jupyter notebook logger
  class JupyterStreamHandler(logging.StreamHandler):
    def emit(self, record):
      log_entry = self.format(record)
      levelname = record.levelname

      if LOG_COLORS.get(levelname) is not None:
        color_format = f"color: {LOG_COLORS.get(levelname)}"
      else:
        color_format = ""

      # Format message as Markdown with color
      display(
        Markdown(f"<span style='font-weight:bold; {color_format}'>{levelname}</span> - {log_entry}")
      )

  class LocalTimezoneFormatter(logging.Formatter):
    """Custom formatter to use the system's local timezone."""

    def formatTime(self, record, datefmt=None):
      # Convert the record's timestamp to the local timezone
      dt = datetime.fromtimestamp(record.created, local_tz)
      if datefmt:
        return dt.strftime(datefmt)
      return dt.isoformat()

  # Format the log messages
  # --------------------------------------
  # Define different formatters
  notebook_fmt = logging.Formatter("%(message)s")  # Simplified for Jupyter

  file_fmt = LocalTimezoneFormatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S UTC%z",
  )

  stream_fmt = LocalTimezoneFormatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S UTC%z",
  )

  # Create log handlers
  # --------------------------------------

  # Jupyter Notebook Logger
  stdoutHandler = JupyterStreamHandler(stream=sys.stdout)
  stdoutHandler.setLevel(int_notebook_level)
  stdoutHandler.setFormatter(notebook_fmt)

  # File output logger
  fileHandler = logging.FileHandler(log_path)
  fileHandler.setLevel(int_file_level)
  fileHandler.setFormatter(file_fmt)

  # Stream output logger
  streamHandler = logging.FileHandler(log_path)
  streamHandler.setLevel(int_file_level)
  streamHandler.setFormatter(stream_fmt)

  # Add handlers to the parent logger
  # --------------------------------------
  logger.addHandler(stdoutHandler)
  logger.addHandler(fileHandler)
  logger.addHandler(streamHandler)

  # Make sure that logger is not filtering at levels below the set level
  logger.setLevel(min(int_file_level, int_notebook_level, int_stream_level))

  logger.debug(
    f"File Log Level: {int_file_level} || Notebook Log Level: {int_notebook_level} || Stream Log Level: {int_stream_level}"
  )

  return logger
