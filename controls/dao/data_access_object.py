from typing import Type, TypeVar, Generic

import json
import os

from controls.tda.list.linked_list import Linked_List


T = TypeVar("T")


class Data_Access_Object(Generic[T]):
    atype: T

    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.url = (
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            + "/data/"
        )

    def _list(self) -> T:
        if os.path.isfile(self.url + self.file):
            with open(self.url + self.file, "r") as f:
                datos = json.load(f)
                self.lista.clear()
                for data in datos:
                    a = self.atype.deserializable(data)
                    self.lista.add(a)
        return self.lista

    def __transform__(self):
        return json.dumps(
            [self.lista.get(i).serializable() for i in range(self.lista._length)],
            indent=4,
        )

    def _to_dict(self):
        aux = []
        self._list()
        for i in range(self.lista._length):
            aux.append(self.lista.get(i).serializable())
        return aux

    def _save(self, data: T) -> None:
        self.lista.add(data)
        with open(self.url + self.file, "w") as a:
            a.write(self.__transform__())

    def _merge(self, data: T, pos) -> None:
        self.lista.update(pos, data)
        with open(self.url + self.file, "w") as a:
            a.write(self.__transform__())

    def _generate_id(self) -> int:
        lista = self._list()
        if lista._length == 0:
            return 0
        else:
            return lista.get(lista._length - 1)._id + 1

    def _get(self, id):
        lista = self._list()
        array = lista.to_array
        for i in range(lista._length):
            if array[i]._id == id:
                return array[i]
        return None
