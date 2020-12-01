from enums import LogLevel, Signal
from gates.Eradicate import Eradicate
from Net import Net
from temporalFissures.Looper import Looper


if __name__ == "__main__":

	net = Net()
	net.logLevel = LogLevel.DEBUG

	nodes = [Eradicate(), Eradicate(), Looper()]
	n1 = [nodes[1], Eradicate()]

	net.addNodeBranch(nodes)
	net.addNodeBranch(n1)

	net.sendSignal(Signal.SB)


# TODO: populate graph
# TODO: use factory for nodes?
