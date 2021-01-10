from enums import LogLevel, Signal
from gates.Eradicate import Eradicate
from Net import Net
from temporalFissures.Looper import Looper


if __name__ == "__main__":

	net = Net()
	net.logLevel = LogLevel.DEBUG

	e0 = Eradicate()
	e1 = Eradicate()
	e2 = Eradicate()
	L0 = Looper()

	e33 = Eradicate()

	branches = [
	[e0, e1, 					e2,						L0],
			[e1,   				Eradicate()],
	[e0, Eradicate(), 							L0],
	[e0, 							e2,    				Eradicate(), e33, Eradicate()],
									 [e2,    				Eradicate()],
	  																					[e33, Eradicate()],
	]
	# branches = [
	# 	[e0, e1],
	# 	[e1, Eradicate()],
	# 	[e1, Eradicate(), Eradicate()],
	# ]


	for b in branches: net.addNodeBranch(b)

	treeLayers = net.straightBranches()

	mapping = {
		Looper: "L",
		Eradicate: "e"
	}
	for tl in treeLayers: print(["-" if a is None else mapping[type(a)] for a in tl])

	# net.sendSignal(Signal.SB)

# TODO: populate graph
# TODO: use factory for nodes?
