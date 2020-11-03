from enums import LogLevel, Signal
from Net import Net

if __name__ == "__main__":

		net = Net()
		# net.logLevel = LogLevel.DEBUG

		net.sendSignal(Signal.SB)

# TODO: populate graph
# TODO: use factory for nodes?
