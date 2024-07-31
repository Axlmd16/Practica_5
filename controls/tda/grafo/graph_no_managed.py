from math import nan
from controls.tda.grafo.adjacent import Adjacent
from controls.tda.grafo.graph_managed import GraphManaged


class GraphNoManaged(GraphManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)

    def insert_edge_w(self, u, v, weight):
        if u <= self.num_vertex and v <= self.num_vertex:
            if not self.exist_edge(u, v):
                edg = self.num_edges + 1
                self.set_num_edge(edg)

                adj1 = Adjacent()
                adj1._destination = v
                adj1._weight = weight

                adj2 = Adjacent()
                adj2._destination = u
                adj2._weight = weight

                self.adjacent(u).add(adj1)
                self.adjacent(v).add(adj2)

            else:
                raise ValueError("Edge already exist")

        else:
            raise ValueError("Vertex out of range")
