import enums.NodeType
import enums.Signal


class TemporalFissure(Node):

	_nodeType = None

	def __init__(self, nodeType):
		super().__init__(self)
		self._nodeType = nodeType

	def __init__(self, nodeType, before,  next):
		super().__init__(self, before, next)
		self._nodeType = nodeType

	def __str__(self):
		return "TemporalFissure {" + self.nodeType + ", id:" + self.__hash__() + "}"


	def addToNext(self, node):
		raise NotImplementedError("Temporal Fissure can not have following nodes")


	def removeFromNext(self, node):
		raise NotImplementedError("Temporal Fissure can not have following nodes")
