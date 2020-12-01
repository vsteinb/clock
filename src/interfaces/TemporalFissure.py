from enums import NodeType, Signal
from interfaces.Node import Node


class TemporalFissure(Node):

	def __init__(self, nodeType):
		super().__init__(nodeType)


	def addToNext(self, node):
		raise NotImplementedError("Temporal Fissure can not have following nodes")


	def removeFromNext(self, node):
		raise NotImplementedError("Temporal Fissure can not have following nodes")
