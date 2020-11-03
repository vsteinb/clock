from enums import NodeType, Signal
from interfaces.TemporalFissure import TemporalFissure


class Looper(TemporalFissure):

	def __init__(self):
		super().__init__(NodeType.TEMPORAL__LOOPER)


	def processSignal(self, signal) -> Signal:
		# TODO
		print(self)
		return signal
