from flask import Blueprint, request, redirect, render_template, url_for, jsonify

from controls.controladores.grafo_parada import GrafoParada
from controls.controladores.parada_control import ParadaControl
from controls.tda.list.linked_list import Linked_List

router = Blueprint("router", __name__)

pc = ParadaControl()
gn = GrafoParada()


@router.route("/grafo")
def grafo():
    return render_template("grafo.html")


@router.route("/grafo_negocio")
def grafo_negocio():
    gn.load_graph()

    return render_template("grafo.html")


@router.route("/grafo_admin")
def grafo_admin():
    negocios = pc.list()
    return render_template("parada/grafo_admin.html", negocios=negocios)


@router.route("/")
def listar_paradas():
    data = pc.list()
    return render_template("parada/lista.html", data=data)


@router.route("/parada/nuevo", methods=["GET", "POST"])
def nueva_parada():
    if request.method == "POST":
        pc._parada._latitud = request.form["latitud"]
        pc._parada._longitud = request.form["longitud"]
        pc._parada._direccion = request.form["direccion"]
        pc._parada._nombre = request.form["nombre"]
        pc.save()
        return redirect(url_for("router.listar_paradas"))

    return render_template("parada/guardar.html")


@router.route("/grafo_admin_matriz", methods=["GET"])
def guardar_adyacencia():
    id_origen = request.args.get("origen")
    id_destino = request.args.get("destino")
    negocios = pc.list()

    if id_origen != id_destino:
        try:
            origen = negocios.search_models_binary("id", int(id_origen))
            destino = negocios.search_models_binary("id", int(id_destino))
            gn.load_graph()

            o = gn.get_grafo().get_vertex(origen)
            d = gn.get_grafo().get_vertex(destino)

            if gn.get_grafo().exist_edge(o, d):
                return jsonify({"error": "Ya existe una adyacencia entre las paradas"})
            else:
                gn.insert_edge(
                    origen,
                    destino,
                    pc.get_distance(
                        origen._latitud,
                        origen._longitud,
                        destino._latitud,
                        destino._longitud,
                    ),
                )
                gn.save_graph()

            matriz = gn.get_adjacency_matrix()
            return jsonify(
                {
                    "success": "Adyacencia guardada correctamente",
                    "matriz": matriz,
                    "negocios": [n._nombre for n in negocios],
                }
            )
        except Exception as e:
            print("Error: ", e)
            return jsonify({"error": "No se pudo guardar la adyacencia"})
    else:
        return jsonify({"error": "Debe seleccionar una parada diferente"})


@router.route("/grafo_admin_matriz_cargar", methods=["GET"])
def cargar_adyacencia():
    gn.load_graph()
    matriz = gn.get_adjacency_matrix()
    negocios = pc.list()
    return jsonify(
        {
            "matriz": matriz,
            "negocios": [n._nombre for n in negocios],
        }
    )


@router.route("/grafo_admin/buscar_camino", methods=["GET"])
def buscar_camino():
    id_origen = request.args.get("origen")
    id_destino = request.args.get("destino")
    tipo = request.args.get("tipo")

    id_origen = int(id_origen) if id_origen is not None else None
    id_destino = int(id_destino) if id_destino is not None else None

    if tipo == "dijkstra":
        predecessor = gn.get_grafo().recorrido_dijkstra(int(id_origen))
        try:
            if predecessor["dist"][id_destino] == float("inf"):
                return jsonify({"error": "No existe una adyacencia entre las paradas"})
            else:
                camino = Linked_List()
                v = id_destino
                while v is not None:
                    camino.add_first(v)
                    v = predecessor["prev"][v]
                gn.get_grafo().print_graph_short(camino)
                return jsonify({"path": camino.to_array})
        except Exception as e:
            print("Error: ", e)
            return jsonify({"error": "No se pudo encontrar el camino"})
    else:
        dist_matrix, next_matrix = gn.get_grafo().recorrido_floyd()
        try:
            if dist_matrix[id_origen][id_destino] == float("inf"):
                return jsonify({"error": "No existe una adyacencia entre las paradas"})
            else:
                camino = Linked_List()
                v = id_origen
                while v != id_destino:
                    camino.add(v)
                    v = next_matrix[v][id_destino]
                camino.add(id_destino)
                gn.get_grafo().print_graph_short(camino)
                return jsonify({"path": camino.to_array})
        except Exception as e:
            print("Error: ", e)
            return jsonify({"error": "No se pudo encontrar el camino"})
