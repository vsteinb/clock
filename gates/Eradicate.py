from enums import NodeType, Signal

import interfaces.Gate
import interfaces.Node

class Eradicate(Gate):

	def __init__(self):
		super().__init__(self, NodeType.GATE__ERADICATE)

	def __init__(self, before, next):
		super().__init__(self, NodeType.GATE__ERADICATE, before, next)

	def processSignal(self, signal) -> Signal:
		# TODO
		return signal
