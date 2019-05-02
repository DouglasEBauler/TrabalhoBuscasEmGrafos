# coding: utf-8
from queue import Queue, Empty
from typing import Dict, List
from enum import Enum


class ColorVertex(Enum):
    WHITE = 0
    SILVER = 1
    BLACK = 2


class Graph:
    def __init__(self):
        self.vertexes: Dict = {}  # Store the vertexes.
        self.queue: Queue = Queue()
        self.time = 0

    def add_vertex(self, key) -> "Vertex":
        if not (key in self.vertexes.keys()):
            self.vertexes[key] = Vertex()

        return self.vertexes[key]

    def clear_queue(self):
        while not self.queue.empty():
            try:
                self.queue.get(False)
            except Empty:
                continue

            self.queue.task_done()

    def internal_dfs(self, vertex: "Vertex"):
        vertex.color = ColorVertex.SILVER
        self.time += self.time
        vertex.distance_origin = self.time

        for v_adj in vertex.adjacent:
            if v_adj.color == ColorVertex.WHITE:
                self.internal_dfs(v_adj)

        vertex.color = ColorVertex.BLACK
        self.time += self.time
        vertex.distance_final = self.time

    def dfs(self):
        self.time = 0

        for v in self.vertexes:
            if v.color == ColorVertex.WHITE:
                self.internal_dfs()

    def bfs(self, vertex_origin: "Vertex"):
        for vertex in self.vertexes:
            vertex.clear()

        vertex_origin.distance_origin = 0
        vertex_origin.color = ColorVertex.SILVER
        self.clear_queue()

        self.queue.put(vertex_origin)

        while not self.queue.empty():
            vertex_q = Vertex(self.queue.get())

            for vertex in vertex_q.list_vertexes_adj:
                if vertex.color == ColorVertex.WHITE:
                    self.insert_queue()
                    vertex.color = ColorVertex.SILVER
                    vertex.parent = vertex_q
                    vertex.distance_origin = vertex_q.distance_origin + 1

            vertex_q.color = ColorVertex.BLACK

    def print_list_adjacent_graph(self) -> str:
        list_adjacent_graph: str = ""

        for key in self.vertexes.keys():
            vertex = self.vertexes[key]
            list_adjacent_vertex = ""
            list_adjacent_vertex += str(key)

            for key_adj in vertex.dict_vertexes_adj.keys():
                if list_adjacent_vertex != "":
                    list_adjacent_vertex += " -> "

                list_adjacent_vertex += "[ " + key_adj + " ] "

            list_adjacent_graph += list_adjacent_vertex + "\n"

        return list_adjacent_graph

    def count_adjacency_by_vertex(self, vertex_i_key, vertex_key_j):
        count_vertex: int = 0

        for key in self.vertexes[vertex_i_key].dict_vertexes_adj.keys():
            if vertex_key_j == key:
                count_vertex += 1

        return count_vertex

    def adjacency_matrix(self):
        if len(self.vertexes) >= 1:
            import numpy as np

            list_vertexes = sorted(self.vertexes.keys())
            adjacency_matrix = np.zeros(shape=(len(self.vertexes), len(self.vertexes)))

            for i in range(len(list_vertexes)):
                for j in range(len(list_vertexes)):
                    adjacency_matrix[i, j] = self.count_adjacency_by_vertex(list_vertexes[i], list_vertexes[j])

            return adjacency_matrix

    def info_graph(self) -> str:
        seq_degrees = self.get_sequence_degrees()
        count_seq_degrees: int = 0
        # seq_degrees_str: str = ""

        for i in seq_degrees:
            count_seq_degrees += i

        return "Número de vérices: " + str(self.vertexes.__len__()) + "\n" + \
               "Número de arestas: " + str(int(count_seq_degrees / 2)) + "\n" + \
               "Sequência de graus: " + str(seq_degrees.__str__())

    def get_sequence_degrees(self) -> List[int]:
        list_seq_degrees: List[int] = []

        for key in self.vertexes.keys():
            vertex = self.vertexes[key]

            list_seq_degrees.append(vertex.dict_vertexes_adj.__len__())

        list_seq_degrees.sort()

        return list_seq_degrees


class Vertex:
    def __init__(self):
        self.distance_origin: int = 0  # Distance origin to the determined a vertex
        self.distance_final: int = 0  # Distance final to the determined a vertex
        self.color: ColorVertex = ColorVertex.WHITE  # Initialize vertex of checked
        self.dict_vertexes_adj: Dict = {}  # Set vertex adjacent
        self.parent: Vertex = None

    def add_adjacent(self, key):
        if not (key in self.dict_vertexes_adj.keys()):
            self.dict_vertexes_adj[key] = Vertex()

    def clear(self):
        self.color = ColorVertex.WHITE
        self.parent = None
        self.distance_origin = 0
        self.distance_final = 0