# coding: utf-8
from graph.classes import Graph
from graph.graph_utils import fill_graph, tree_graph


if __name__ == '__main__':
    # Fill graph
    graph = fill_graph("../question_1/test1.txt")

    vertex_key = input("Informe o vértice inicial para realização das buscas: ")
    try:
        g = graph.pop()
        queue = g.dfs(g.vertex_list[vertex_key])
        tree_graph(graph, "dfs", "../question_1/info_graph.txt", queue)

        g.bfs(graph.vertex_list[vertex_key])
        tree_graph(graph, "bfs", "../question_1/info_graph.txt")
    except Exception:
        print("Vértice não encontrado")
