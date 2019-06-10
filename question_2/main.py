from time import time
from question_2.graph import Graph


def print_matrix(g):
    for vertice in g.graph.items():
        print(vertice)


def fill_graph(file_name: str):
    f = open(file_name, "r")

    if f.__sizeof__() == 0:
        raise FileExistsError("Arquivo do grafo não está preenchido")

    g = Graph()

    for line in f:
        line = line.replace("\n", "")
        values = line.split(" ", 2)

        # Add edge
        g.add_edge(values[0], (values[1], int(values[2])))

    return g


def main():
    g = fill_graph("../question_2/input.txt")
    g.dfs(0)
    print("Vértices de grau impar: ", g.impares)

    odds_v = Graph()  # Grafo dos vértices de grau ímpar

    for i in g.impares:
        linha = g.dijkstra(i)
        for j in g.impares:
            odds_v.add_edge(i, (j, linha[j]))

    print("Menores caminhos entre os vértices de grau ímpar:\n")
    print_matrix(odds_v)

    print("Grafo com as arestas duplicadas:\n")
    print_matrix(g)

    if not g.is_connected(0):
        if g.euleriano():
            cycle, cust = g.fleury("0")
            print(cycle)
            print(cust)


if __name__ == '__main__':
    t = time()
    main()
    t = (time() - t) / 1000
    print('Tempo de execução: {}ms'.format(t))
