# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
import sys

from graph.graph_utils import fill_graph


def print_result(graph_list: {}):
    try:
        f = open("../question_2/dengue_result.txt", "w")
    except FileNotFoundError:
        f = open("../question_2/dengue_result.txt", "x")

    for key, value in graph_list.items():
        f.write("Teste " + str(key) + "\n")
        f.write(value.name + "\n")
        f.write("\n")

    f.close()


if __name__ == '__main__':
    # Fill graph
    graphs = fill_graph("../question_2/dengue.txt")

    vertex_result_list = {
        "1": None,
        "2": None,
        "3": None
    }

    g_index = 1

    while graphs:
        g = graphs.pop(0)

        vertex_result = None
        min_level: int = sys.maxsize

        for v in sorted(g.vertex_list):
            vertex_v = g.vertex_list[v]

            g.bfs(vertex_v)

            d_max: int = sys.maxsize * -1

            for w in g.vertex_list:
                vertex_w = g.vertex_list[w]

                if vertex_w.distance > d_max:
                    d_max = vertex_w.distance

            if d_max < min_level:
                min_level = d_max
                vertex_result = vertex_v

        vertex_result_list[str(g_index)] = vertex_result
        g_index += 1

    print_result(vertex_result_list)
