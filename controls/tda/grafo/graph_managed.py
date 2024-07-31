from controls.tda.grafo.adjacent import Adjacent
from controls.tda.grafo.grafo import Graph
from controls.tda.list.linked_list import Linked_List
from math import nan


class GraphManaged(Graph):
    def __init__(self, num_vert) -> None:
        super().__init__()
        self.__num_vertex = num_vert
        self.__num_edges = 0
        self.__list_adjacent = []

        for i in range(0, num_vert):
            self.__list_adjacent.append(Linked_List())

    def set_num_edge(self, num_edge):
        self.__num_edges = num_edge

    @property
    def num_vertex(self):
        return self.__num_vertex

    @property
    def num_edges(self):
        return self.__num_edges

    def exist_edge(self, u, v):
        band = False
        if u <= self.__num_vertex and v <= self.__num_vertex:
            adj = self.__list_adjacent[u]
            if not adj.is_empty:
                array = adj.to_array
                for i in range(0, adj._length):
                    adj = array[i]
                    if adj._destination == v:
                        band = True
                        break
        else:
            raise ValueError("Vertex out of range")
        return band

    def weight_edge(self, u, v):
        weight = None
        if self.exist_edge(u, v):
            adj = self.__list_adjacent[u]
            array = adj.to_array
            for i in range(0, adj._length):
                adj = array[i]
                if adj._destination == v:
                    weight = adj._weight
                    break
        else:
            raise ValueError("Edge not exist")
        return weight

    def insert_edge_w(self, u, v, weight):
        if u <= self.__num_vertex and v <= self.__num_vertex:
            if not self.exist_edge(u, v):
                self.__num_edges += 1

                adj = Adjacent()
                adj._destination = v
                adj._weight = weight
                self.__list_adjacent[u].add(adj)
                self.print_graph()

            else:
                raise ValueError("Edge already exist")
        else:
            raise ValueError("Vertex out of range")

    def insert_edge(self, u, v):
        self.insert_edge_w(u, v, nan)

    def adjacent(self, u):
        return self.__list_adjacent[u]
