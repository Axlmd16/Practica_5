from controls.tda.list.linked_list import Linked_List


class StackOP(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verify_top(self):
        return self._length < self.__tope

    def push(self, data):
        if self.verify_top:
            self.add_pos(data, 0)
        else:
            raise Exception("Stack Full")

    @property
    def pop(self):
        if self.is_empty:
            raise Exception("Stack Empty")
        else:
            self.delete(0)
