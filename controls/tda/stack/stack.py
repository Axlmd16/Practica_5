from controls.tda.stack.stackOp import StackOP


class Stack:
    def __init__(self, size):
        self.__stack = StackOP(size)

    def pop(self):
        return self.__stack.pop

    def push(self, data):
        return self.__stack.push(data)

    def print(self):
        return self.__stack.print

    def verify(self):
        return self.__stack.verify_top
