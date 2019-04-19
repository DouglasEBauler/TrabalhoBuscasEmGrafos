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

    def add_vertex(self, vertex: "Vertex"):
        self.vertextes.append(vertex)

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


class Vertex:
    def __init__(self, value: object):
        self.value: object = value  # Store the value of the vertex
        self.distance_origin: int = 0  # Distance origin to the determined a vertex
        self.distance_final: int = 0  # Distance final to the determined a vertex
        self.color: ColorVertex = ColorVertex.WHITE  # Initialize vertex of checked
        self.list_vertexes_adj: List[Vertex] = []  # Set vertex adjacent
        self.parent: Vertex = Vertex()

    def clear(self):
        self.color = ColorVertex.WHITE
        self.parent = None
        self.distance_origin = 0
        self.distance_final = 0
