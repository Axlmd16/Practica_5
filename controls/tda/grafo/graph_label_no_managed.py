from controls.tda.grafo.adjacent import Adjacent
from controls.tda.grafo.graph_label_managed import GraphLabelManaged


class GraphLabelNoManaged(GraphLabelManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)

    def insert_edge_w_label(self, label1, label2, weight):

        u = self.get_vertex(label1)
        v = self.get_vertex(label2)

        if u != -1 and v != -1:
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

                    self.print_graph()

                else:
                    raise ValueError("Edge already exist")

        else:
            raise ValueError("No se encontro el vertice")

