from itertools import chain

from enums import LogLevel, Signal
from gates.Eradicate import Eradicate
from Net import Net
from temporalFissures.Looper import Looper


def straightBranches(layers):

	activeBranches = []
	treeLayers = []
	for layerIndex, layer in enumerate(layers):

		# no commits left
		if not len(layer):
			print("Layer is empty!?")
			return

		# initial layer
		if layerIndex == 0:
			activeBranches = layer

		# all others
		else:

			for commit in layer:

				# got no parent!?
				if not len(commit.parents):
					print("What the fuck?")
					continue

				# if commit is the first child of a parent, continue that column
				foundPlace = False
				for parent in commit.parents:
					if parent.children[0] == commit:

						# replace parent by commit in branches
						index = activeBranches.index(parent)
						activeBranches[index] = commit
						commit.j = index
						foundPlace = True
						break
				if foundPlace:
					continue

				# TODO check if a merge commit destroys the order. e.g. if it is the first child of two parents at the same time.
				# that would eventually result in commits of those branches to be blocked

				# compute free j-coordinates
				freeColumns = [index for index, value in enumerate(
					activeBranches) if value == None]

				if len(freeColumns):

					# occupy free column by commit in activeBranches
					# !TODO make the choosing more intelligent
					activeBranches[activeBranches.index(freeColumns[0])] = commit
				else:
					# insert commit
					activeBranches.append(commit)

			# purge all ended branches of activeBranches
			for index in range(len(activeBranches)):
				if activeBranches[index] not in layer:
					activeBranches[index] = None

		treeLayers.append(activeBranches)

	return treeLayers





if __name__ == "__main__":

	net = Net()
	net.logLevel = LogLevel.DEBUG

	nodes = [Eradicate(), Eradicate(), Eradicate(), Looper()]
	n1 = 								  [nodes[1],   Eradicate()]
	n2 = 		[nodes[0],    Eradicate(), nodes[2]]
	n3 = 		[nodes[0], nodes[3]]

	net.addNodeBranch(nodes)
	net.addNodeBranch(n1)
	net.addNodeBranch(n2)
	net.addNodeBranch(n3)

	#net.sendSignal(Signal.SB)

	# print(nodes, n2, n3, n1)
	layers = net.cleanTree()
	for layer in layers: print([l.__str__() for l in layer])
	print()
	treeLayers = straightBranches(layers)
	for tl in treeLayers: print([a.__str__() for a in tl])

# TODO: populate graph
# TODO: use factory for nodes?
