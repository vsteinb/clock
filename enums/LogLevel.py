from enum import Enum, unique

@unique
class LogLevel(Enum):
	DEBUG = 0
	INFO = 1
	WARN = 2
	ERROR = 3
