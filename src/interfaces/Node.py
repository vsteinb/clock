from abc import ABC, abstractmethod

from enums import Signal


# interface, implemented by gate & temporal fissure
class Node(ABC):

	# init with empty _before- & _next relations
	def __init__(self, nodeType):
		self._nodeType = nodeType
		self._before = []
		self._next = []


	def getNext(self): return self._next


	# returns null if the signal didn't pass through
	@abstractmethod
	def processSignal(self, s: Signal):
		pass


	def __str__(self):
		return "{" + self._nodeType.name + ", hash:" + self.__hash__().__str__() + "}"


	# destroy this node after rewiring _before & after nodes to each other
	def destroy(self):
		# TODO how rewire?
		pass


	# needed if neighbors are destroyed
	# IMPORTANT: automatic management of _before every time _next is changed!
	def addToNext(self, node):

		if node in self._next: return

		self._next.append(node)
		node._addToBefore(self)


	def removeFromNext(self, node):

		# remove node (all duplicates if existing)
		indices = [index for index, value in enumerate(self._next) if value == node]
		for index in indices:
			del self._next[index]

		# apply in reverse, too
		node._removeFromBefore(self)



	# private starting here

	def _addToBefore(self, node):

		if node in self._before: return

		self._before.append(node)


	def _removeFromBefore(self, node):
		# remove node (all duplicates if existing)
		indices = [index for index, value in enumerate(self._before) if value == node]
		for index in indices:
			del self._before[index]
