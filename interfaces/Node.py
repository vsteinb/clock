from abc import ABC, abstractmethod

from enums import Signal


# interface, implemented by gate & temporal fissue
class Node(ABC):

	# both lists contain only (other) Nodes
	_before = []
	_next = []

	# init with empty _before- & _next relations
	def __init__(self): pass


	# _before & _next are Node-Lists (Node[])
	def __init__(self, _before, _next):
		self._before = _before
		self._next = _next


	def getNext(self): return self._next


	# need to override
	# returns null if the signal didn't pass through
	@abstractmethod
	def processSignal(self, s: Signal):
		pass


	# need to override
	@abstractmethod
	def __str__(self):
		pass


	# destroy this node after rewiring _before & after nodes to each other
	def destroy(self):
		# TODO how rewire?
		pass


	# needed if neighbors are destroyed
	def removeFrom_beforeNodes(self, node):
		# remove node (all duplicates if existing)
		self._before.removeAll(node)

		# apply in reverse, too
		node.removeFromNext(self)


	def removeFromNext(self, node):

		# remove node (all duplicates if existing)
		self._next.removeAll(node)

		# apply in reverse, too
		node.removeFromBeforeNodes(self)


	def addToBeforeNodes(self, node):
		if node in self._before: return

		self._before.add(node)
		node.addToNext(self)


	def addToNext(self, node):
		if node in self._next: return

		self._next.add(node)
		node.addToBeforeNodes(self)


# TODO: automatic management of _before every time _next is changed
