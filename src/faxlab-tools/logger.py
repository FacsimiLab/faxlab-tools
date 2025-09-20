import logging
import os
import uuid
import datetime
import json

class LoggerFactory:
    def __init__(self, base_log_dir="logs", context=None):
        self.base_log_dir = base_log_dir
        self.context = context or {}
        self.date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        self.uuid_str = str(uuid.uuid4())
        self.log_dir = os.path.join(self.base_log_dir, self.date_str)
        os.makedirs(self.log_dir, exist_ok=True)
        self.logger = logging.getLogger(self.uuid_str)
        self.logger.handlers.clear()
        self.logger.setLevel(logging.DEBUG)
        self._add_handlers()

    def _add_handlers(self):
        # Human-readable log
        human_log_path = os.path.join(self.log_dir, f"{self.uuid_str}.log")
        human_handler = logging.FileHandler(human_log_path)
        human_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        human_handler.setFormatter(human_formatter)
        self.logger.addHandler(human_handler)

        # Machine-readable JSON log
        json_log_path = os.path.join(self.log_dir, f"{self.uuid_str}.json")
        json_handler = logging.FileHandler(json_log_path)
        json_formatter = ContextJsonFormatter(self.context)
        json_handler.setFormatter(json_formatter)
        self.logger.addHandler(json_handler)

    def get_logger(self):
        return self.logger

class ContextJsonFormatter(logging.Formatter):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            **self.context
        }
        return json.dumps(log_record)
