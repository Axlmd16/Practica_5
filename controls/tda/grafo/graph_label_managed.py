from math import nan
from controls.tda.grafo.graph_managed import GraphManaged


class GraphLabelManaged(GraphManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)
        self.__labels = [None]
        self.__labels_vertex = {}
        for _ in range(num_vert):
            self.__labels.append(None)

    def get_vertex(self, label):
        try:
            return self.__labels_vertex[str(label)]
        except KeyError:
            return -1

    def label_vertex(self, v, label):
        self.__labels[v] = label
        self.__labels_vertex[str(label)] = v

    def get_label(self, v):
        return self.__labels[v]

    def exist_edge_label(self, label1, label2):
        u = self.get_vertex(label1)
        v = self.get_vertex(label2)
        if u != -1 and v != -1:
            return self.exist_edge(u, v)
        else:
            return False

    def insert_edge_w_label(self, label1, label2, weight):
        u = self.get_vertex(label1)
        v = self.get_vertex(label2)
        if u != -1 and v != -1:
            self.insert_edge_w(u, v, weight)
        else:
            raise ValueError("Vertex not exist")

    def insert_edge_label(self, label1, label2):
        self.insert_edge_w_label(label1, label2, nan)

    def weight_edge_label(self, label1, label2):
        u = self.get_vertex(label1)
        v = self.get_vertex(label2)
        if u != -1 and v != -1:
            return self.weight_edge(u, v)
        else:
            raise ValueError("Vertex not exist")

    def adjacent_label(self, label):
        u = self.get_vertex(label)
        if u != -1:
            return self.adjacent(u)
        else:
            raise ValueError("Vertex not exist")

    def __str__(self) -> str:
        out = ""
        for i in range(self.num_vertex):
            out += f"Vertex {str(i)}: \n"
            adjs = self.adjacent(i)
            for j in range(adjs._length):
                out += f"\t{adjs.to_array[j]}\n"
        return out
