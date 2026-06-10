## <summary> This class reperesents a log entry, it is an entity.
import enum
from enum import Enum
class Log:
    def __init__(self, log_id: int, service_name: str, level: str, message: str, timestamp: str):
        self.log_id = log_id
        self.service_name = service_name
        self.level = level
        self.message = message
        self.timestamp = timestamp

    class LogLevel(str, Enum):
        INFO = "INFO"
        WARNING = "WARNING"
        ERROR = "ERROR"
        DEBUG = "DEBUG"
        FATAL = "FATAL"