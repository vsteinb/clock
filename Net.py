from enums import Signal, LogLevel
from interfaces.Node import Node


class Net:

	def __init__(self):
			self.startNode = None


	# recursive walk through graph
	# breadth-first search
	# in case of loop structures: stop if previously visited was hit
	def sendSignal(self, signal: Signal):
		if not self.startNode: return

		initialLayer = [(signal, self.startNode)]
		self._sendSignal(initialLayer, [])


	def _sendSignal(self, layer, history):

		nextLayer = []
		for signal, toNode in layer:

			# detected loop, stop here
			if toNode in history: continue

			# gate processes signal
			processedSignal = toNode.processSignal(signal)
			history.append(toNode)

			# signal did not pass through, stop here
			if processedSignal is None: continue

			# add next nodes to new layer
			for n in toNode.getNext():
				nextLayer.append((processedSignal, n))
		print()
		# process underlying layers
		if nextLayer: self._sendSignal(nextLayer, history)



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
