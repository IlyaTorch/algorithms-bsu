from collections import defaultdict
# Задание 3.1.
# Граф G задан списками смежностей вершин.
# Найти компоненты связности графа G.
# Определить, является ли граф G эйлеровым;
# если граф G - эйлеров, построить эйлеров цикл.
# Определить, является ли граф G двудольным;
# если G - двудольный, найти разбиение на доли.


class Graph:

    def __init__(self, vertices):
        self.num_of_vertices = vertices
        self.graph = defaultdict(list)
        self.visited_list = []
        self.component_index_list = []
        self.num_of_components = 0
        self._euler_cycle = []
        self.euler_cycle = []

        self.colors = [None for _ in range(self.num_of_vertices)]

    def is_euler(self) -> bool:
        for adjacent_vertices in self.graph.values():
            if len(adjacent_vertices) % 2:
                return False
        return True

    def depth_first_search(self, vertex) -> None:
        self.component_index_list[vertex] = self.num_of_components
        self.visited_list[vertex] = True
        for adjacent_vertex in self.graph[vertex]:
            if not self.visited_list[adjacent_vertex]:
                self.depth_first_search(adjacent_vertex)

    def find_connectivity_components(self) -> list:
        self.visited_list = [False] * self.num_of_vertices
        self.component_index_list = [-1] * self.num_of_vertices
        self.num_of_components = 0

        for vertex in range(self.num_of_vertices):
            if not self.visited_list[vertex]:
                self.depth_first_search(vertex)
                self.num_of_components += 1
        return self.component_index_list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def find_euler_cycle(self, vertex=0):
        if self.is_euler():
            if len(self._euler_cycle) == 0 or vertex != self._euler_cycle[-1]:
                self._euler_cycle.append(vertex)

                for adjacent_vertex in self.graph[vertex]:
                    self.remove_edge(vertex, adjacent_vertex)
                    self.find_euler_cycle(adjacent_vertex)
                if not self.graph[vertex]:
                    self.euler_cycle.append(vertex)
                    del(self._euler_cycle[-1])
                    if self._euler_cycle:
                        self.find_euler_cycle(self._euler_cycle[-1])

    def is_bipartite(self, vertex, color):
        # depth_first_search modification
        self.colors[vertex] = color

        for adjacent_vertex in self.graph[vertex]:
            if self.colors[adjacent_vertex] is None:
                self.is_bipartite(adjacent_vertex, int(not color))
            elif self.colors[adjacent_vertex] == color:
                return False
        return True

    def find_parts_if_bipartite(self):
        for vertex in range(self.num_of_vertices - 1):
            if self.colors[vertex] is None:
                if not self.is_bipartite(vertex, 1):
                    print('Graph is not bipartite')
                    return False
        return self.colors


if __name__ == '__main__':
    # graph = Graph(9)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(1, 2)
    # # graph.add_edge(1, 6)
    # graph.add_edge(1, 6)
    # graph.add_edge(1, 7)
    # graph.add_edge(2, 3)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 4)
    # graph.add_edge(4, 5)
    # graph.add_edge(4, 7)
    # # graph.add_edge(5, 6)
    # graph.add_edge(5, 6)
    # graph.add_edge(5, 7)
    # graph.add_edge(5, 8)
    # # graph.add_edge(5, 8)
    # # graph.add_edge(6, 7)
    # graph.add_edge(6, 7)
    # graph.add_edge(6, 8)
    # # print(graph.is_euler())
    # # print(graph.find_connectivity_components())
    # # graph.find_euler_cycle()
    # # print(graph.euler_cycle)
    # print(graph.find_parts_if_bipartite())

    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 6)
    graph.add_edge(2, 4-1)
    graph.add_edge(2, 4)
    graph.add_edge(4-1, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    print(graph.find_parts_if_bipartite())
