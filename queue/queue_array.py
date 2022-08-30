class EmptyQueueErr(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 5
    
    def __init__(self) -> None:
        # initially set all underlying elems to None
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY

        # number of available (not None) elems
        self._size = 0

        # current index at front queue
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyQueueErr("Empty queue")
        
        return self._data[self._front]

    def getQueue(self):
        return self._data, self._size, self._front

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueErr("Empty queue")

        # get current elem at current front
        removedItem = self._data[self._front]

        # set current front elem to None
        self._data[self._front] = None

        # update front to point to next index
        self._front = (self._front + 1) % len(self._data)

        # decrease size
        self._size -= 1

        # return the old current elem
        return removedItem

    def enqueue(self, elem):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        # append new elem to end of queue
        newElemIndex = (self._front + self._size) % len(self._data)
        self._data[newElemIndex] = elem

        # increase size
        self._size += 1

    def _resize(self, cap):
        # get old queue's _data --> oldQueueData
        oldQueueData = self._data

        # set new queue's _data to double len of None elems
        self._data = [None] * cap

        # get old queue's front --> oldFront
        oldFront = self._front

        # loop i through old queue's _size
        for i in range(self._size):
            # set newQueue[i] = oldQueueData[oldFront]
            self._data[i] = oldQueueData[oldFront]

            # set oldFront = (oldFront + 1) % len(oldQueueData)
            oldFront = (oldFront + 1) % len(oldQueueData)

        # set new queue's front = 0
        self._front = 0

myQueue = ArrayQueue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.getQueue())

myQueue.enqueue(4)
myQueue.enqueue(5)
print(myQueue.getQueue())

myQueue.enqueue(6)
myQueue.enqueue(7)
print(myQueue.getQueue())

myQueue.enqueue(8)
myQueue.enqueue(9)
print(myQueue.getQueue())