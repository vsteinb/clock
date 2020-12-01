from enum import Enum, unique


# enum with gate & temporal fissure types
@unique
class NodeType(Enum):
	GATE__ERADICATE = 0
	TEMPORAL__LOOPER = 100


@unique
class Signal(Enum):
	SB = 0


@unique
class LogLevel(Enum):
	DEBUG = 0
	INFO = 1
	WARN = 2
	ERROR = 3
