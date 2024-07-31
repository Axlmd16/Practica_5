from controls.tda.queue.queueOp import QueueOp


class Queue:
    def __init__(self, size):
        self.__queue = QueueOp(size)

    def dequeue(self):
        return self.__queue.dequeue

    def queue(self, data):
        return self.__queue.queue(data)

    def print(self):
        return self.__queue.print

    def verify(self):
        return self.__queue.verify_top
