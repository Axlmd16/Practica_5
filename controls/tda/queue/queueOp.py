from controls.tda.list.linked_list import Linked_List


class QueueOp(Linked_List):
    def __init__(self, top):
        super().__init__()
        self.__ = top

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verify_top(self):
        return self._length < self.__top

    def queque(self, data):
        if self.verify_top:
            self.add_pos(data, self._length)
        else:
            raise Exception("Queue Full")

    @property
    def dequeue(self):
        if self.is_empty:
            raise Exception("Queue Empty")
        else:
            self.delete(0)
