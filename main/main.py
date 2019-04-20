from graph.classes import Graph, Vertex


def fill_graph() -> Graph:
    f = open("../question1/test1.txt", "r")

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
            vertex = g.add_vertex(Vertex(vertexes[0]))
            vertex_adj = Vertex(vertexes[1])

            vertex.add_adjacent(vertex_adj)

    return g


def info_graph(g: Graph):
    try:
        f = open("../question1/info_graph.txt", "r")
    except FileNotFoundError:
        f = open("../question1/info_graph.txt", "x")

    f.write(g.info_graph())
    f.close()


if __name__ == '__main__':
    graph = fill_graph()

    info_graph(graph)
