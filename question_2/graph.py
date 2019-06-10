from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.pares = []
        self.impares = []
        self.peso = 0
        self.graph = defaultdict(set)
        self.graph_size = 0

    def add_edge(self, u, v):
        self.graph[u].add(v)
        temp = max(u, v[0])
        if int(temp) > self.graph_size:
            self.graph_size = int(temp)

    def rmv_edge(self, u, v):
        for vertex in self.graph[u]:
            if vertex[0] == v:
                self.graph[u].discard(v)

    def dfs_util(self, v, visited):
        visited[v][0] = True
        if (len(self.graph[v])-1) % 2:
            visited[v][2] += 1
            self.impares.append(v)
        else:
            visited[v][1] += 1
            self.pares.append(v)

        for i in self.graph[v]:
            if not visited[i[0]][0]:
                self.dfs_util(i[0], visited)

    def dfs(self, v):
        visited = [[False, 0, 0] for temp in range(
            self.graph_size + 1)]
        self.dfs_util(v, visited)

        return visited

    def bfs(self, v):
        visited = [False] * (self.graph_size + 1)
        queue = []

        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            for i in self.graph[v]:
                if not visited[i[0]]:
                    print(i[0])
                    queue.append(i[0])
                    visited[i[0]] = True

    def dijkstra(self, x):
        distance = [1000] * (self.graph_size + 1)
        visited = [False] * (self.graph_size + 1)
        pq = []
        heapq.heapify(pq)

        distance[x] = 0
        heapq.heappush(pq, (0, x))

        while len(pq) > 0:
            aux = heapq.heappop(pq)
            a = aux[1]

            if visited[a]:
                continue
            visited[a] = True

            for u in self.graph[a]:
                b = u[0]
                w = u[1]

                if distance[a] + w < distance[b]:
                    distance[b] = distance[a] + w
                    heapq.heappush(pq, (distance[b], b))
        return distance

    def is_connected(self, v):
        visited = self.dfs(v)
        num_v_visited = 0
        for i in range(len(visited)):
            num_v_visited += 1
        return self.graph_size == num_v_visited

    def euleriano(self):
        for v in self.graph:
            vertex = self.graph[v]
            if (len(vertex) - 1) % 2 != 0:
                return False
            else:
                return True

    def num_vertex(self):
        return len(self.graph)

    def is_valid_next_edge(self, v, u):
        if len(self.graph[v]) == 1:
            return True

        cust = u[1]
        u = u[0]

        visited = [False] * self.num_vertex()
        c1 = self.dfs_count(v, visited)

        self.rmv_edge(u, v)
        self.rmv_edge(v, u)

        visited = [False] * self.num_vertex()
        c2 = self.dfs_count(v, visited)

        self.add_edge(v, (u, cust))
        self.add_edge(u, (v, cust))

        return c2 <= c1

    def dfs_count(self, v, visited):
        count = 1
        visited[int(v)] = True

        for i in self.graph[v]:
            if not visited[0]:
                count += self.dfs_count(i[0], visited)
        return count

    def num_edges(self):
        m = 0

        for v in self.graph:
            vertex = self.graph[v]
            m += len(vertex)
        return m

    def fleury(self, v):
        cycle = [v]
        cust = 0

        while self.num_edges() != 0:
            for u in self.graph[v]:
                if self.is_valid_next_edge(v, u):
                    cycle.append(u[0])
                    cust += u[1]
                    self.rmv_edge(u, v)
                    self.rmv_edge(v, u)
                    v = u[0]
                    break

        return cycle, cust
