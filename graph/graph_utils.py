# coding: utf-8
from graph.classes import Graph, Vertex


def fill_graph(file_name: str) -> []:
    f = open(file_name, "r")

    if f.__sizeof__() == 0:
        raise FileExistsError("Arquivo do grafo não está preenchido")

    list_graph = []
    g = None

    for line in f:
        vertexes = line.split(" ", 1)

        try:
            vertexes[1]
        except Exception:
            vertexes[0] = vertexes[0].replace("\n", "")

            if vertexes[0] == "0":
                break
            elif vertexes[0] == "1":
                list_graph.append(g)
                g = None

                g = Graph()
                g.add_vertex(Vertex(vertexes[0]))
                list_graph.append(g)
                g = None
            elif g is None:
                g = Graph()
            else:
                list_graph.append(g)
                g = None
                g = Graph()

            continue
        else:
            vertexes[0] = vertexes[0].replace("\n", "")
            vertexes[1] = vertexes[1].replace("\n", "")

            # Add vertex in graph
            g.add_vertex(Vertex(vertexes[0]))
            g.add_vertex(Vertex(vertexes[1]))

            # Add edge
            g.add_edge(vertexes[0], vertexes[1])

    if g not in list_graph:
        list_graph.append(g)

    return list_graph


def info_graph(g: Graph, file_name: str):
    try:
        f = open(file_name, "a")
    except FileNotFoundError:
        f = open(file_name, "x")

    f.write(g.info_graph())
    f.write("")
    f.close()


def tree_graph(g: Graph, type_search: str, file_name: str, queue=[]):
    tree_str: str = ""

    if type_search == "bfs":
        for key in g.vertex_list:
            vertex: Vertex = g.vertex_list[key]

            if tree_str != "":
                tree_str += "\n"

            if vertex.parent is None:
                tree_str += vertex.name + " -> [ Parent: nil ]"
            else:
                tree_str += vertex.name + " -> [ Parent: " + str(vertex.parent.name) + ", Level: " + str(vertex.distance) + " ]"

    try:
        f = open(file_name, "a")
    except FileNotFoundError:
        f = open(file_name, "x")

    if type_search == "dfs":
        f.write("----------Busca em profundidade---------- \n")
    elif type_search == "bfs":
        f.write("----------Busca em largura--------------- \n")
    f.write(tree_str)
    if type_search == "dfs":
        f.write("Queue -> " + str(queue.__str__()))
    f.write("\n \n")
    f.close()
