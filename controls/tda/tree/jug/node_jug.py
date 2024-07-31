from controls.tda.list.linked_list import Linked_List
from models.jarras.jug import Jug


class NodeJug:
    def __init__(self) -> None:
        self.__jb = Jug()
        self.__jl = Jug()
        self.__father = None
        self.__successors = Linked_List()

        self.__jb._capacity = 4
        self.__jb._current_capacity = 0

        self.__jl._capacity = 3
        self.__jl._current_capacity = 0

    @property
    def _jb(self):
        return self.__jb

    @_jb.setter
    def _jb(self, value):
        self.__jb = value

    @property
    def _jl(self):
        return self.__jl

    @_jl.setter
    def _jl(self, value):
        self.__jl = value

    @property
    def _father(self):
        return self.__father

    @_father.setter
    def _father(self, value):
        self.__father = value

    @property
    def _successors(self):
        return self.__successors

    @_successors.setter
    def _successors(self, value):
        self.__successors = value

    def set_current_capacity(self, jb, jl):
        self.__jb._current_capacity = jb
        self.__jl._current_capacity = jl

    def __str__(self) -> str:
        return f"Jb: {self.__jb},\nJl: {self.__jl}"
