# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
from graph.classes import Graph, Vertex


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
