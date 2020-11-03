from enum import Enum, unique

# enum with gate & temporal fissure types
@unique
class NodeType(Enum):
	GATE__ERADICATE = 0
	TEMPORAL__LOOPER = 100
