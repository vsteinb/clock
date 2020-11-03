from enums import NodeType, Signal
from interfaces.Gate import Gate


class Eradicate(Gate):

	def __init__(self):
		super().__init__(NodeType.GATE__ERADICATE)


	def processSignal(self, signal) -> Signal:
		# TODO
		print(self, signal)
		return signal
