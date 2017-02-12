class MinHeap:
	'''
	An implementation of a min-heap using a list that 
	can store an object at each node.
	Each entry is a tuple of the form (int, data).
	'''

	def __init__(self, iterable=[]):
		''' (MinHeap, iterable) -> NoneType
		Constructor for this MinHeap. Takes an optional iterable object
		to initialize this MinHeap.

		REQ: elements of iterable MUST be of the for (int, data).
		'''

		self._heap = []

		for elem in iterable:
			try:

				#TODO: create a heapify method for better performance.
				self.insert(elem)
			except TypeError:
				raise InvalidHeapEntry("Heap entry MUST be of \
the form (int, data")

	def insert(self, num, elem):
		''' (MinHeap, int, object) -> NoneType
		Inserts the element elem into this min-heap.
		'''

		# check if the element being inserted is of the right form
		if isinstance(elem[0], float):
			raise InvalidHeapEntry("Heap index MUST be a number.")
		
		self._heap.append(elem)
		self._shiftUp(len(self._heap)-1)

	def extractMin(self):
		''' (MinHeap) -> object
		Returns the element in this min-heap with the lowest value.
		'''

		if self._heap:
			self._swap(0, len(self._heap)-1)
			res = self._heap.pop()
			self._shiftDown(0)
			return res[1]

	def findMin(self):
		''' (MinHeap) -> tuple of (int, object)
		Returns the min element of this min-heap without removing 
		it from this min-heap.
		'''

		return self._heap[0]

	def update(self, num, elem):
		''' (Graph, object) -> NoneType
		Updates the index of element elem to num.
		'''

		for i in range(len(self._heap)):
			
			if self._heap[i][1] == elem:
				self._heap[i][0] = num
				self._shiftUp(i)
				self._shiftDown(i)
				break

	def isEmpty(self):
		''' (MinHeap) -> bool
		Returns True iff this min-heap is empty, False otherwise.
		'''

		return not self._heap

	#helper functions
	def _shiftUp(self, index):
		
		parent = (index-1) // 2

		if parent >= 0 and self._heap[parent][0] > self._heap[index][0]:
			self._swap(parent, index)
			self._shiftUp(parent)

	def _shiftDown(self, index):

		left = 2*index + 1
		right = 2*index + 2

		if (right < len(self._heap) and 
			self._heap[right][0] < self._heap[left][0] and
			self._heap[right][0] < self._heap[index][0]):

			self._swap(index, right)
			self._shiftDown(right)

		elif (left < len(self._heap) and
			self._heap[left][0] < self._heap[index][0]):

			self._swap(index, left)
			self._shiftDown(left)

	def _swap(self, i, j):
		self._heap[i], self._heap[j] = self._heap[j], self._heap[i]



class InvalidHeapEntry(Exception):
	''' 
	Custom Exception for invalid Heap entry.
	'''
	pass


if __name__ == "__main__":
	h = MinHeap([(10,10), (2,2), (3,3), (7,7)])
	h.insert((5,5))
	print(h.extractMin())
	print(h.extractMin())
	print(h.extractMin())
	print(h.extractMin())

	import random as r
	randomL = [(1000-i ,1000-i) for i in range(1000)]

	heap = MinHeap(randomL)
	L = [heap.extractMin() for i in randomL]
	randomL.sort()
	print(L == [i[0] for i in randomL])

