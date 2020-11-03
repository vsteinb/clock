import enums.LogLevel
from enums import Signal, LogLevel

import interfaces.Node



class Net:

	# Singleton, cannot make constructor private, therefore nested class
	class _Net:

		# has no instance vars
		def __init__(self): pass

	# typeof Net
	_instance = None

	def __init__(self):
		if not Net._instance:
			Net._instance = Net._Net()


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
			history.add(toNode)

			# signal did not pass through, stop here
			if processedSignal is None: continue

			# add next nodes to new layer
			for n in toNode.getNext():
				nextLayer.add((processedSignal, n))

		# process underlying layers
		self._sendSignal(nextLayer, history)



	def _addGate(self):		# randomGate, random location (set next[] on new and existing nodes)
		# TODO
		pass

	def _addTemporalFissue(self):		# random fissue after random gate (not fissue, should not have nodes after)
		# TODO
		pass
