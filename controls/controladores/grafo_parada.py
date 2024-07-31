import json
import os

from controls.controladores.parada_control import ParadaControl
from controls.tda.grafo.graph_label_no_managed import GraphLabelNoManaged
from controls.tda.list.linked_list import Linked_List


class GrafoParada:
    def __init__(self) -> None:
        self.__grafo = None
        self.__nc = ParadaControl()
        self.__url = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../data")
        )
        self.__url_file = os.path.join(self.__url, "grafo_parada.json")

    def is_exist_file(self) -> bool:
        return os.path.isfile(self.__url_file)

    def save_graph(self):
        grafo_dict = {
            "num_vertex": self.__grafo.num_vertex,
            "num_edges": self.__grafo.num_edges,
            "list_adjacent": [],
        }
        aristas = Linked_List()
        for i in range(self.__grafo.num_vertex):
            for edge in self.__grafo.adjacent(i):
                origen_id = min(i, edge._destination)
                destino_id = max(i, edge._destination)
                arista = (origen_id, destino_id)
                if arista not in aristas.to_array:
                    aristas.add_last(arista)
                    grafo_dict["list_adjacent"].append(
                        {
                            "vertex_id": origen_id,
                            "destination_id": destino_id,
                        }
                    )

        with open(self.__url_file, "w") as f:
            json.dump(grafo_dict, f, indent=4)

    def load_graph(self):
        if self.is_exist_file():
            try:
                paradas = self.__nc.list()
                with open(self.__url_file, "r") as f:
                    grafo_dict = json.load(f)
                    self.__grafo = GraphLabelNoManaged(self.__nc.list()._length)

                    # Etiquetar los vértices
                    for item in paradas.to_array:
                        self.__grafo.label_vertex(item._id, item)

                    for edge in grafo_dict["list_adjacent"]:
                        origen = paradas.search_models_binary("id", edge["vertex_id"])
                        destino = paradas.search_models_binary(
                            "id", edge["destination_id"]
                        )
                        peso = self.__nc.get_distance(
                            origen._latitud,
                            origen._longitud,
                            destino._latitud,
                            destino._longitud,
                        )
                        self.__grafo.insert_edge_w_label(origen, destino, peso)
            except Exception as e:
                print(e)
        else:
            print("No existe el archivo")
            self.create_graph()

    def create_graph(self):
        lista = self.__nc.list()
        if lista._length > 0:
            self.__grafo = GraphLabelNoManaged(lista._length)
            array = lista.to_array
            for i in range(lista._length):
                self.__grafo.label_vertex(i, array[i])
            self.__grafo.print_graph()
            self.save_graph()

    def insert_edge(self, origen, destino, peso):
        self.__grafo.insert_edge_w_label(origen, destino, peso)

    def get_adjacency_matrix(self):
        num_vertex = self.__grafo.num_vertex
        matrix = [[0] * num_vertex for _ in range(num_vertex)]
        for i in range(num_vertex):
            for edge in self.__grafo.adjacent(i):
                matrix[i][edge._destination] = edge._weight
        return matrix

    def get_grafo(self):
        return self.__grafo
