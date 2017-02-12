from minheap import MinHeap, InvalidHeapEntry

class MinPQueue:
	'''
	A min-priority Queue implementation using a min-heap.
	Each entry is a tuple of the form (priority_number, data).
	'''

	def __init__(self, iterable=[]):
		''' (MinPQueue, iterable) -> NoneType
		Constructor for this MinPQueue. Takes an optional iterable object
		to initialize this MinPQueue.

		REQ: elements of iterable MUST be of the for (priority_number, data).
		'''

		try: 
			self._queue = MinHeap(iterable) 
		except InvalidHeapEntry:
			raise InvalidQueueEntry("Queue entry MUST be of \
the form (priority_number, data)")

	def insert(self, priority, elem):
		''' (MinPQueue, tuple of (int, object)) -> NoneType
		Inserts the element elem into this min-priority queue.
		'''

		self._queue.insert(priority, elem)

	def popMin(self):
		''' (MinPQueue) -> object
		Returns the object from the queue with the minimum priority.
		'''

		return self._queue.extractMin()

	def peek(self):
		''' (MinPQueue) -> tuple of (int, object)
		Returns the element with the lowest priority without removing 
		it from the queue with the priority.
		'''

		return self._queue.findMin()

	def update(self, priority, elem):
		''' (MinPQueue, num, object) -> NoneType
		Updates the element elem's priority with num.
		'''

		self._queue.update(priority, elem)

	def isEmpty(self):
		''' (MinPQueue) -> bool
		Returns True iff this min-priority queue is empty, False otherwise.
		'''

		return self._queue.isEmpty()



class InvalidQueueEntry(Exception):
	''' 
	Custom Exception for invalid Queue entry.
	'''
	pass
