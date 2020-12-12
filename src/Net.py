from enums import Signal, LogLevel
from interfaces.Node import Node


class Net:

	def __init__(self):
			self.startNode = None
			self.layers = []


	# recursive walk through graph
	# breadth-first search
	# in case of loop structures: stop if previously visited was hit
	def sendSignal(self, signal: Signal):
		if not self.startNode: return

		initialLayer = [(signal, self.startNode)]
		self._sendSignal(initialLayer)


	def _sendSignal(self, layer):

		nextLayer = []
		for signal, toNode in layer:

			# gate processes signal
			processedSignal = toNode.processSignal(signal)

			# signal did not pass through, stop here
			if processedSignal is None: continue

			# add next nodes to new layer
			for n in toNode.getNext():
				nextLayer.append((processedSignal, n))
		print()
		# process underlying layers
		if nextLayer: self._sendSignal(nextLayer)



	def _addGate(self):		# randomGate, random location (set next[] on new and existing nodes)
		# TODO
		pass


	def _addTemporalFissue(self):		# random fissue after random gate (not fissue, should not have nodes after)
		# TODO
		pass


	def _removeNode(self, node):
		node.destroy()


	def addNodeBranch(self, nodes):

		if not nodes: return

		for i in range(len(nodes) - 1 ):

			node = nodes[i]
			nextNode = nodes[i+1]

			node.addToNext(nextNode)

		if self.startNode is None: self.startNode = nodes[0]

		self._cleanTree()


	# recursive walk through graph
	# breadth-first search
	# in case of loop structures: stop if previously visited was hit
	def _cleanTree(self):
		if not self.startNode: return

		layers = self.__cleanTree([set([self.startNode])], [])
		self.layers = layers
		self._cleanup()


	def __cleanTree(self, layers, history):

		nextLayer = []
		currentLayer = layers[-1]
		deleteFromCurrentLayer = []

		for toNode in currentLayer:

			# detected loop, stop here
			if toNode in history:
				deleteFromCurrentLayer.append(toNode)
				continue

			# gate processes signal
			history.append(toNode)

			# add next nodes to new layer
			for n in toNode.getNext():
				nextLayer.append(n)

		# postprocess current layer
		for n in deleteFromCurrentLayer:
			currentLayer.remove(n)

		# process underlying layers recursively
		if nextLayer:
			layers.append(set(nextLayer))
			return self.__cleanTree(layers, history)

		# deepest layer found, return from recursion
		return layers if len(layers[-1]) else layers[:-1]


	def _cleanup(self):
		for index, layer in enumerate(self.layers):

			# gotten to last layer, delete all potential children since there is no layer afterwards
			if index + 1 >= len(self.layers):
				for node in layer:
					children = node._next
					for child in children:
						node.removeFromNext(child)
				continue

			# see if a child is still in the cleaned-up version. if not, delete reference of parent
			parents = layer
			current = self.layers[index + 1]

			for parent in parents:
				allChildren = parent._next

				for child in allChildren:
					if child not in current:
						parent.removeFromNext(child)


	def straightBranches(self):

		activeBranches = []
		treeLayers = []
		for layerIndex, layer in enumerate(self.layers):
			layer = list(layer)

			# no commits left
			if not len(layer):
				print("Layer is empty!?")
				break

			# initial layer
			if layerIndex == 0:
				activeBranches = layer

			# all others
			else:

				for commit in layer:

					# got no parent!?
					if not len(commit._before):
						print("What the fuck?")
						continue

					# if commit is the first child of a parent, continue that column
					foundPlace = False
					for parent in commit._before:
						if parent._next[0] == commit:

							# replace parent by commit in branches
							index = activeBranches.index(parent)
							activeBranches[index] = commit
							# commit.j = index
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
						activeBranches[freeColumns[0]] = commit
					else:
						# insert commit
						activeBranches.append(commit)

				# purge all ended branches of activeBranches
				for index in range(len(activeBranches)):
					if activeBranches[index] not in layer:
						activeBranches[index] = None

			treeLayers.append([b for b in activeBranches])

		return treeLayers
