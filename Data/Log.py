## <summary> This class reperesents a log entry, it is an entity.
import enum
from enum import Enum
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlmodel import Field

class Base(DeclarativeBase):
    pass
class Log(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str] = mapped_column (String(255))
    level: Mapped[str] = mapped_column(String(50))
    message: Mapped[str] = mapped_column(String(255))
    timestamp: Mapped[str] = mapped_column(String(255))

class LogLevel(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    FATAL = "FATAL"