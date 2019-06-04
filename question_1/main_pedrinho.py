# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
from graph.classes import Graph, Vertex


def fill_graph(file_name: str) -> Graph:
    f = open(file_name, "r")

    if f.__sizeof__() == 0:
        raise FileExistsError("Arquivo do grafo não está preenchido")

    g = Graph()

    for line in f:
        line = line.replace("\n", "")
        values = line.split(" ", 2)

        try:
            values[2]
        except Exception:
            g.destiny_vertex = str(int(values[0]) + 1)  # Destiny vertex
            continue
        else:
            # Add vertex in graph
            g.add_vertex(Vertex(values[0]))
            g.add_vertex(Vertex(values[1]))

            # Add edge
            g.add_edge(values[0], values[1], int(values[2]))

    return g


def info_graph(g: Graph, file_name: str):
    try:
        f = open(file_name, "w")
    except FileNotFoundError:
        f = open(file_name, "x")

    g.dijsktra("0")

    f.write(str(g.vertex_list[g.destiny_vertex].distance))
    f.close()


if __name__ == '__main__':
    # fill graph
    graph = fill_graph("../question_1/input.txt")

    # save info graph
    info_graph(graph, "C:/Temp/entrada.in.txt")