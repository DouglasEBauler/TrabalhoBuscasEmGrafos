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
            vertexes[0] = vertexes[0].replace("\n", "")
            vertexes[1] = vertexes[1].replace("\n", "")

            vertex_0 = g.add_vertex(vertexes[0])  # Add vertex in graph
            vertex_1 = g.add_vertex(vertexes[1])

            vertex_0.add_adjacent(vertexes[1])  # Add vertex adjacent in vertex
            vertex_1.add_adjacent(vertexes[0])  # Add vertex adjacent in vertex

    return g


def info_graph(g: Graph):
    try:
        f = open("../question1/info_graph.txt", "w")
    except FileNotFoundError:
        f = open("../question1/info_graph.txt", "x")

    f.write(g.info_graph())
    f.close()


if __name__ == '__main__':
    graph = fill_graph()

    info_graph(graph)

    option = input("Como deseja representar o grafo?(1 = lista de ajdjacência, 2 = matriz) \n")

    if option == "1":
        print(graph.print_list_adjacent_graph())
    elif option == "2":
        print(graph.adjacency_matrix())
