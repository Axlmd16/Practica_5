import os
import time

from controls.tda.list.linked_list import Linked_List


class Graph:
    """
    La clase Graph define una estructura de datos abstracta para representar grafos.
    Esta clase es una interfaz y debe ser implementada por subclases que especifiquen la
    representación concreta del grafo (e.g., lista de adyacencia, matriz de adyacencia).
    """

    @property
    def num_vertex(self):
        """
        Devuelve el número de vértices en el grafo.
        :return: Número de vértices.
        """
        raise NotImplementedError("Please Implement this method")

    @property
    def num_edges(self):
        """
        Devuelve el número de aristas en el grafo.
        :return: Número de aristas.
        """
        raise NotImplementedError("Please Implement this method")

    def exist_edge(self, u, v):
        """
        Verifica si existe una arista entre dos vértices dados.
        :param u: Vértice de origen.
        :param v: Vértice de destino.
        :return: True si existe la arista, False en caso contrario.
        """
        raise NotImplementedError("Please Implement this method")

    def weight_edge(self, u, v):
        """
        Devuelve el peso de la arista entre dos vértices dados.
        :param u: Vértice de origen.
        :param v: Vértice de destino.
        :return: Peso de la arista.
        """
        raise NotImplementedError("Please Implement this method")

    def insert_edge(self, u, v):
        """
        Inserta una arista sin peso entre dos vértices dados.
        :param u: Vértice de origen.
        :param v: Vértice de destino.
        """
        raise NotImplementedError("Please Implement this method")

    def insert_edge_w(self, u, v, weight):
        """
        Inserta una arista con un peso dado entre dos vértices.
        :param u: Vértice de origen.
        :param v: Vértice de destino.
        :param weight: Peso de la arista.
        """
        raise NotImplementedError("Please Implement this method")

    def adjacent(self, u):
        """
        Devuelve la lista de vértices adyacentes a un vértice dado.
        :param u: Vértice de origen.
        :return: Lista de vértices adyacentes.
        """
        raise NotImplementedError("Please Implement this method")

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del grafo, mostrando los vértices y sus adyacentes.
        :return: Representación en cadena del grafo.
        """
        out = ""
        for i in range(self.num_vertex):
            out += f"Vertex {str(i)}: \n"
            adjs = self.adjacent(i)
            for j in range(adjs._length):
                out += f"\t{adjs.to_array[j]}\n"
        return out

    def print_graph(self):
        """
        Genera un archivo JavaScript para visualizar el grafo usando la librería d3.js.
        Crea nodos y aristas, y escribe el código en un archivo .js.
        Ahora soporta grafos etiquetados.
        :return: Ruta del archivo generado.
        """
        # Ruta del archivo .js que se generará.
        path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../static")
        )
        path = os.path.join(path, r"d3\grafo.js")

        data = ""
        # Definición de nodos en el archivo .js
        data += "var nodes = ([\n"
        for i in range(self.num_vertex):
            label = self.get_label(i) if self.get_label(i) is not None else i
            data += f"  {{id: {i}, label: '{label}'}},\n"
        data += "]);\n\n"

        # Definición de aristas en el archivo .js
        data += "var edges = ([\n"
        for i in range(self.num_vertex):
            adjs = self.adjacent(i)
            for j in range(adjs._length):
                dest_label = (
                    self.get_label(adjs.to_array[j]._destination)
                    if self.get_label(adjs.to_array[j]._destination) is not None
                    else adjs.to_array[j]._destination
                )
                data += f"  {{from: {i}, to: {adjs.to_array[j]._destination}, label: '{adjs.to_array[j]._weight}'}},\n"
        data += "]);\n\n"

        # Generación del código JavaScript para visualización
        js = ""
        js += "var data = {\n"
        js += "  nodes: nodes,\n"
        js += "  edges: edges,\n"
        js += "};\n"
        js += "var container = document.getElementById('mynetwork');\n"
        js += "var options = {};\n"
        js += "var network = new vis.Network(container, data, options);\n"

        # Escritura en el archivo
        try:
            with open(path, "w") as file:
                file.write(data)
                file.write(js)
        except Exception as e:
            print(e)

    def print_graph_short(self, camino_corto):
        """
        Genera un archivo JavaScript para visualizar el grafo usando la librería d3.js y pintar de rojo el camino más corto.
        Crea nodos y aristas, y escribe el código en un archivo .js.
        Ahora soporta grafos etiquetados.
        :return: Ruta del archivo generado.
        """
        # Ruta del archivo .js que se generará.
        path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../static")
        )
        path = os.path.join(path, r"d3\grafo.js")

        data = ""
        # Definición de nodos en el archivo .js
        data += "var nodes = ([\n"
        for i in range(self.num_vertex):
            label = self.get_label(i) if self.get_label(i) is not None else i
            data += f"  {{id: {i}, label: '{label}'}},\n"
        data += "]);\n\n"

        # Definición de aristas en el archivo .js
        data += "var edges = ([\n"
        for i in range(self.num_vertex):
            adjs = self.adjacent(i)
            for j in range(adjs._length):
                dest_label = (
                    self.get_label(adjs.to_array[j]._destination)
                    if self.get_label(adjs.to_array[j]._destination) is not None
                    else adjs.to_array[j]._destination
                )
                data += f"  {{from: {i}, to: {adjs.to_array[j]._destination}, label: '{adjs.to_array[j]._weight}'}},\n"
        data += "]);\n\n"

        # Generación del código JavaScript para visualización
        js = ""
        js += "var data = {\n"
        js += "  nodes: nodes,\n"
        js += "  edges: edges,\n"
        js += "};\n"
        js += "var container = document.getElementById('mynetwork');\n"
        js += "var options = {};\n"
        js += "var network = new vis.Network(container, data, options);\n"

        # Pintar de rojo el camino más corto
        js += "var camino = ["
        for i in range(camino_corto._length):
            js += f"{camino_corto[i]}"
            if i < camino_corto._length - 1:
                js += ", "
        js += "];\n"
        js += "network.on('afterDrawing', function(ctx) {\n"
        js += "  for (var i = 0; i < camino.length - 1; i++) {\n"
        js += "    var node1 = network.getPositions([camino[i]])[camino[i]];\n"
        js += "    var node2 = network.getPositions([camino[i + 1]])[camino[i + 1]];\n"
        js += "    ctx.strokeStyle = 'red';\n"
        js += "    ctx.lineWidth = 3;\n"
        js += "    ctx.beginPath();\n"
        js += "    ctx.moveTo(node1.x, node1.y);\n"
        js += "    ctx.lineTo(node2.x, node2.y);\n"
        js += "    ctx.stroke();\n"
        js += "  }\n"
        js += "});\n"

        # Escritura en el archivo
        try:
            with open(path, "w") as file:
                file.write(data)
                file.write(js)
        except Exception as e:
            print(e)

    def recorrido_dijkstra(self, s) -> dict:
        start = time.time()
        dist = Linked_List()
        prev = Linked_List()
        visited = Linked_List()

        for _ in range(self.num_vertex):
            dist.add_last(float("inf"))
            prev.add_last(None)
            visited.add_last(False)

        dist.update(s, 0)

        for _ in range(self.num_vertex):
            u = self.min_distance(dist.to_array, visited.to_array)

            if u == -1:
                break

            visited.update(u, True)

            for v in range(self.num_vertex):
                if (
                    not visited[v]
                    and self.exist_edge(u, v)
                    and dist[u] + self.weight_edge(u, v) < dist[v]
                ):
                    dist.update(v, dist[u] + self.weight_edge(u, v))
                    prev.update(v, u)

        end = time.time()
        print(f"Algoritmo de Dijkstra: {end - start} segundos")
        return {"dist": dist.to_array, "prev": prev.to_array}

    def min_distance(self, dist, visited):
        min_dist = float("inf")
        min_index = -1

        for v in range(len(dist)):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v

        return min_index

    def recorrido_floyd(self):
        start = time.time()
        num_vertex = self.num_vertex
        dist_matrix = Linked_List()
        next_matrix = Linked_List()

        for _ in range(num_vertex):
            dist_matrix.add_last(Linked_List())
            next_matrix.add_last(Linked_List())
            for _ in range(num_vertex):
                dist_matrix.get_last().add_last(float("inf"))
                next_matrix.get_last().add_last(None)

        for i in range(num_vertex):
            dist_matrix[i].update(i, 0)

        for i in range(num_vertex):
            for j in range(num_vertex):
                if self.exist_edge(i, j):
                    dist_matrix[i].update(j, self.weight_edge(i, j))
                    next_matrix[i].update(j, j)

        for k in range(num_vertex):
            for i in range(num_vertex):
                for j in range(num_vertex):
                    if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                        dist_matrix[i].update(j, dist_matrix[i][k] + dist_matrix[k][j])
                        next_matrix[i].update(j, next_matrix[i][k])

        end = time.time()
        print(f"Algoritmo de Floyd: {end - start} segundos")

        return dist_matrix.to_array, next_matrix.to_array
