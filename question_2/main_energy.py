# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
from graph.classes import Graph, Vertex, ColorVertex


def fill_graph_list(file_name: str) -> []:
    f = open(file_name, "r")

    if f.__sizeof__() == 0:
        raise FileExistsError("Arquivo do grafo não está preenchido")

    list_graph = []
    count_edges: int = 0
    g = None

    for line in f:
        if line.replace("\n", "") == "0 0":
            break

        if count_edges == 0:
            params = line.split(" ", 1)

            params[0] = params[0].replace("\n", "")
            params[1] = params[1].replace("\n", "")

            count_edges = int(params[1])
            count_vertex = int(params[0])+1
            vertexes_list = sorted([str(i) for i in range(1, count_vertex)])
        else:
            if g is None:
                g = Graph()

            while vertexes_list:
                g.add_vertex(Vertex(vertexes_list.pop(0)))

            if count_edges > 0:
                vertexes = line.split(" ", 1)

                vertexes[0] = vertexes[0].replace("\n", "")
                vertexes[1] = vertexes[1].replace("\n", "")

                # Add edge
                if vertexes[0] in g.vertex_list and vertexes[1] in g.vertex_list:
                    g.add_edge(vertexes[0], vertexes[1])

                count_edges -= 1
                if count_edges == 0:
                    list_graph.append(g)
                    g = None
            else:
                list_graph.append(g)
                g = None

    return list_graph


def print_result(test_list: {}):
    try:
        f = open("../question_2/energy_result.txt", "w")
    except FileNotFoundError:
        f = open("../question_2/dengue_result.txt", "x")

    for key, value in test_list.items():
        f.write("Teste " + str(key) + "\n")
        if value:
            f.write("falha \n")
        else:
            f.write("normal \n")

        f.write("\n")

    f.close()


if __name__ == '__main__':
    graph = fill_graph_list("../question_2/energy.txt")

    graph_test_dfs = {
        "1": False,
        "2": False
    }

    g_list_key: int = 1
    fail: bool = False
    visited = []

    while graph:
        g: Graph = graph.pop(0)
        for v in sorted(g.vertex_list):
            visited = g.dfs(g.vertex_list[v])
            break

        for v in g.vertex_list:
            if v not in visited:
                fail = True
                break

        graph_test_dfs[str(g_list_key)] = fail
        g_list_key += 1

    print_result(graph_test_dfs)
