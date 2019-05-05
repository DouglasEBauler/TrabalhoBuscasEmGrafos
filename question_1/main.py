# coding: utf-8
from graph.classes import Graph
from graph.graph_utils import fill_graph, info_graph


if __name__ == '__main__':
    # Fill graph
    graph = fill_graph("../question_1/test1.txt")

    g = graph.pop()

    # save info graph
    info_graph(g, "../question_1/info_graph.txt")

    option = input("Como deseja representar o grafo?(1 = lista de ajdjacência, 2 = matriz) \n")

    if option == "1":
        print(g.list_adjacent_graph())
    elif option == "2":
        print(g.adjacency_matrix())