# coding: utf-8
# author: Douglas Eduardo Bauler, Jefferson do Nascimento Júnior.
import sys
from typing import Dict, List
from enum import Enum


class ColorVertex(Enum):
    WHITE = 0
    SILVER = 1
    BLACK = 2


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors: List = []
        self.distance: int = 0  # Distance origin to the determined a vertex
        self.color: ColorVertex = ColorVertex.WHITE  # Initialize vertex of checked
        self.parent: Vertex = None

    def add_neighbor(self, v: "Vertex"):
        n_set = set(self.neighbors)

        if v not in n_set:
            self.neighbors.append(v)
            self.neighbors.sort()

    def clear(self):
        self.distance = 0
        self.color = ColorVertex.WHITE
        self.parent = None


class Graph:
    def __init__(self):
        self.vertex_list: Dict = {}  # Store the vertexes.
        self.edges: Dict = {}
        self.destiny_vertex = ""

    def clear_vertexes(self):
        for key in self.vertex_list:
            self.vertex_list[key].clear()

    def add_vertex(self, vertex: Vertex):
        if vertex.name not in self.vertex_list:
            self.vertex_list[vertex.name] = vertex

    def add_edge(self, u, v, value: int = 0):
        if u in self.vertex_list and v in self.vertex_list:
            self.vertex_list[u].add_neighbor(v)
            self.vertex_list[v].add_neighbor(u)

            self.edges[u, v] = value

    def list_adjacent_graph(self) -> str:
        list_adjacent_str: str = ""
        for key in sorted(self.vertex_list.keys()):
            if list_adjacent_str != "":
                list_adjacent_str += "\n"

            list_adjacent_str += key + " -> " + str(self.vertex_list[key].neighbors)

        return list_adjacent_str

    def count_adjacency_by_vertex(self, vertex_name_i, vertex_name_j):
        count_vertex: int = 0

        for vertex in self.vertex_list[vertex_name_i].neighbors:
            if vertex_name_j == vertex:
                count_vertex += 1

        return count_vertex

    def adjacency_matrix(self):
        if len(self.vertex_list) >= 1:
            import numpy as np

            list_vertexes = sorted(self.vertex_list.keys())
            adjacency_matrix = np.zeros(shape=(len(self.vertex_list), len(self.vertex_list)), dtype=int)

            for i in range(len(list_vertexes)):
                for j in range(len(list_vertexes)):
                    adjacency_matrix[i, j] = self.count_adjacency_by_vertex(list_vertexes[i], list_vertexes[j])

            return adjacency_matrix

    def dfs(self, vertex: Vertex) -> []:
        stack = [vertex.name]
        visited = set()

        while stack:
            v = self.vertex_list[stack.pop()]

            if v.name in visited:
                continue

            visited.add(v.name)
            for w in reversed(v.neighbors):
                if self.vertex_list[w].name not in visited:
                    stack.append(w)

        return visited

    def bfs(self, vertex: Vertex):
        self.clear_vertexes()
        queue = []
        vertex.distance = 0
        vertex.color = ColorVertex.SILVER

        queue.append(vertex.name)
        while len(queue) > 0:
            u = queue.pop(0)
            vertex_u = self.vertex_list[u]

            for v in vertex_u.neighbors:
                vertex_v = self.vertex_list[v]

                if vertex_v.color == ColorVertex.WHITE:
                    queue.append(v)

                    vertex_v.color = ColorVertex.SILVER
                    vertex_v.parent = vertex_u
                    vertex_v.distance = vertex_u.distance + 1

            vertex_u.color = ColorVertex.BLACK

    def dijsktra(self, v_initial: Vertex):
        self.vertex_list[v_initial].distance = 0
        self.vertex_list[v_initial].parent = None

        for key in self.vertex_list.keys():
            if not key == v_initial:
                self.vertex_list[key].distance = sys.maxsize  # represent distance infinity
                self.vertex_list[key].parent = None

        queue_v_calculate = []
        queue = self.vertex_list.copy()

        while queue:
            vertex = min([value for key, value in queue.items()], key=lambda vertex: vertex.distance)
            del queue[vertex.name]
            queue_v_calculate.append(vertex)

            for v_adj in vertex.neighbors:
                try:
                    distance_edge = self.edges[(vertex.name, v_adj)]
                except KeyError:
                    distance_edge = self.edges[(v_adj, vertex.name)]

                if self.vertex_list[v_adj].distance > vertex.distance + distance_edge:
                    self.vertex_list[v_adj].distance = vertex.distance + distance_edge
                    self.vertex_list[v_adj].parent = vertex

    def get_sequence_degrees(self) -> List[int]:
        list_seq_degrees: List[int] = []

        for key in self.vertex_list.keys():
            vertex = self.vertex_list[key]

            list_seq_degrees.append(vertex.neighbors.__len__())

        return sorted(list_seq_degrees)

    def info_graph(self) -> str:
        seq_degrees = self.get_sequence_degrees()
        count_seq_degrees: int = 0

        for i in seq_degrees:
            count_seq_degrees += i

        return "Número de vérices: " + str(self.vertex_list.__len__()) + "\n" + \
               "Número de arestas: " + str(int(count_seq_degrees / 2)) + "\n" + \
               "Sequência de graus: " + str(seq_degrees.__str__())
