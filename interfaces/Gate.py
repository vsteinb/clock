import enums.NodeType


class Gate(Node):

	# of type nodeType
	_nodeType = None

	def __init__(self, nodeType):
		super().__init__(self)
		self._nodeType = nodeType

	def __init__(self, nodeType, before, next):
		super().__init__(self, before, next)
		self._nodeType = nodeType

	def __str__(self):
		return "Gate {" + self.nodeType + ", id:" + self.__hash__() + "}"
