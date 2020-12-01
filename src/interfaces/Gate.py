from enums import NodeType
from interfaces.Node import Node


class Gate(Node):

	def __init__(self, nodeType):
		super().__init__(nodeType)
