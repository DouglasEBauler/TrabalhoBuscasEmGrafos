# coding: utf-8
from graph.classes import Graph, Vertex


def fill_graph(file_name: str) -> Graph:
    f = open(file_name, "r")

    if f.__sizeof__() == 0:
        raise FileExistsError("Arquivo do grafo não está preenchido")

    g = Graph()

    for line in f:
        vertexes = line.split(" ", 1)

        try:
            vertexes[1]
        except Exception:
            continue
        else:
            vertexes[0] = vertexes[0].replace("\n", "")
            vertexes[1] = vertexes[1].replace("\n", "")

            # Add vertex in graph
            g.add_vertex(Vertex(vertexes[0]))
            g.add_vertex(Vertex(vertexes[1]))

            # Add edge
            g.add_edge(vertexes[0], vertexes[1])

    return g


def info_graph(g: Graph, file_name: str):
    try:
        f = open(file_name, "w")
    except FileNotFoundError:
        f = open(file_name, "x")

    f.write(g.info_graph())
    f.write("")
    f.close()


def tree_graph(g: Graph, type_search: str, file_name: str):
    tree_str: str = ""

    for key in g.vertex_list:
        vertex: Vertex = g.vertex_list[key]

        if tree_str != "":
            tree_str += "\n"

        if vertex.parent is None:
            tree_str += vertex.name + " -> [ Parent: nil, "
        else:
            tree_str += vertex.name + " -> [ Parent: " + str(vertex.parent.name) + ", "

        if type_search == "dfs":
            tree_str += "Level: " + str(vertex.distance_origin) + "/" + str(vertex.distance_final) + " ]"
        elif type_search == "bfs":
            tree_str += "Level: " + str(vertex.distance_origin) + " ]"

    try:
        f = open(file_name, "w")
    except FileNotFoundError:
        f = open(file_name, "x")

    f.write(tree_str)
    f.write("")
    f.close()
