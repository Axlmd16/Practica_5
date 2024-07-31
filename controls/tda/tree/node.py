class Node:
    def __init__(self, data) -> None:
        self.__data = data
        self.__father = None
        self.__left = None
        self.__right = None

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, value):
        self.__data = value

    @property
    def _father(self):
        return self.__father

    @_father.setter
    def _father(self, value):
        self.__father = value

    @property
    def _left(self):
        return self.__left

    @_left.setter
    def _left(self, value):
        self.__left = value

    @property
    def _right(self):
        return self.__right

    @_right.setter
    def _right(self, value):
        self.__right = value

    def __str__(self) -> str:
        return str(self.__data)
