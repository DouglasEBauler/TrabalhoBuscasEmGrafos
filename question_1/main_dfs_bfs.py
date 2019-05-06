# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
from graph.graph_utils import fill_graph, tree_graph
import time


def elapsed_since(start):
    #return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))
    elapsed = time.time() - start
    if elapsed < 1:
        return str(round(elapsed*1000, 2)) + "ms"
    if elapsed < 60:
        return str(round(elapsed, 2)) + "s"
    if elapsed < 3600:
        return str(round(elapsed/60, 2)) + "min"
    else:
        return str(round(elapsed / 3600, 2)) + "hrs"


if __name__ == '__main__':
    # Fill graph
    graph = fill_graph("../question_1/test1.txt")

    vertex_key = input("Informe o vértice inicial para realização das buscas: ")
    try:
        startTime = time.time()
        g = graph.pop()
        queue = g.dfs(g.vertex_list[vertex_key])
        tree_graph(g, "dfs", "../question_1/info_graph.txt", queue)
        print("DFS time:" + elapsed_since(startTime))

        g.bfs(g.vertex_list[vertex_key])
        tree_graph(g, "bfs", "../question_1/info_graph.txt")
        print("BFS time:" + elapsed_since(startTime))
    except Exception:
        print("Vértice não encontrado")
