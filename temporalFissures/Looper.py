import interfaces.Node
import interfaces.TemporalFissure
from enums import NodeType, Signal


class Looper(TemporalFissure):

	def __init__(self):
		super().__init__(self, NodeType.TEMPORAL__LOOPER)

	def __init__(self, before, next):
		super().__init__(self, NodeType.TEMPORAL__LOOPER, before, next)


	def processSignal(self, signal) -> Signal:
		# TODO
		return signal
