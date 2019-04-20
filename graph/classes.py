from queue import Queue, Empty
from typing import List
from enum import Enum


class ColorVertex(Enum):
    WHITE = 0
    SILVER = 1
    BLACK = 2


class Graph:
    def __init__(self):
        self.vertexes: List[Vertex] = []  # Store the vertexes.
        self.queue: Queue = Queue()
        self.time = 0

    def add_vertex(self, vertex: "Vertex") -> "Vertex":
        if not self.is_contains(vertex):
            self.vertexes.append(vertex)

        return self.vertexes[self.vertexes.index(vertex)]

    def is_contains(self, vertex: "Vertex"):
        for o in self.vertexes:
            if o.value == vertex.value:
                return True

        return False

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

        for vertex in self.vertexes:
            list_adjacent_vertex = ""
            list_adjacent_vertex += vertex.value

            for vertex_adj in vertex.list_vertexes_adj:
                if list_adjacent_vertex != "":
                    list_adjacent_vertex += " -> "

                list_adjacent_vertex += "[ " + vertex_adj.value + " ] "

            list_adjacent_graph += list_adjacent_vertex + "\n"

        return list_adjacent_graph

    def info_graph(self) -> str:
        seq_degrees = self.get_sequence_degrees()
        count_seq_degrees: int = 0

        for i in seq_degrees:
            count_seq_degrees += int(i)

        return "Número de vérices: " + self.vertexes.__sizeof__() + "\n" + \
               "Número de arestas: " + ((self.vertexes.__sizeof__() + count_seq_degrees) / 2) + "\n" + \
               "Sequência de graus: " + seq_degrees

    def get_sequence_degrees(self) -> List[int]:
        list_seq_degrees: List[int] = []

        for vertex in self.vertexes:
            list_seq_degrees.append(vertex.list_vertexes_adj.__sizeof__())

        list_seq_degrees.sort()

        return list_seq_degrees


class Vertex:
    def __init__(self, value: object):
        self.value: object = value  # Store the value of the vertex
        self.distance_origin: int = 0  # Distance origin to the determined a vertex
        self.distance_final: int = 0  # Distance final to the determined a vertex
        self.color: ColorVertex = ColorVertex.WHITE  # Initialize vertex of checked
        self.list_vertexes_adj: List[Vertex] = []  # Set vertex adjacent
        self.parent: Vertex = None

    def add_adjacent(self, vertex: "Vertex"):
        if not self.is_contains(vertex):
            self.list_vertexes_adj.append(vertex)

    def is_contains(self, vertex_adj: "Vertex"):
        for vertex in self.list_vertexes_adj:
            if vertex.value == vertex_adj.value:
                return True

        return False

    def clear(self):
        self.color = ColorVertex.WHITE
        self.parent = None
        self.distance_origin = 0
        self.distance_final = 0
