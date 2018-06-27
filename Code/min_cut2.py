# https://stackoverflow.com/questions/23825200/karger-min-cut-algorithm-in-python-2-7
# https://www.google.co.uk/search?q=Karger%27s+algorithm&rlz=1C1RLNS_enGB763GB763&oq=Karger%27s+algorithm&aqs=chrome..69i57j69i61&sourceid=chrome&ie=UTF-8
# https://rajsain.files.wordpress.com/2013/11/randomized-algorithms-motwani-and-raghavan.pdf
# https://www.youtube.com/watch?v=wmPuTX2Wlgs

import random, copy
from random import randint

class KargerMinCutter:
    def __init__(self, graph_file):
        self._graph = {}
        self._total_edges = 0
        with open(graph_file) as file:
            for index, line in enumerate(file):
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]
                self._total_edges += len(numbers[1:])

    def find_min_cut(self):
        min_cut = 0
        final_edge = 0
        while len(self._graph) > 2:
            v1, v2 = self._pick_random_edge()
            self._total_edges -= len(self._graph[v1])
            self._total_edges -= len(self._graph[v2])
            self._graph[v1].extend(self._graph[v2])
            for vertex in self._graph[v2]:
                self._graph[vertex].remove(v2)
                self._graph[vertex].append(v1)
            self._graph[v1] = list(filter(lambda v: v != v1, self._graph[v1]))
            self._total_edges += len(self._graph[v1])
            self._graph.pop(v2)
        for edges in self._graph.values():
            min_cut = len(edges)
        return min_cut

    def _pick_random_edge(self):
        rand_edge = randint(0, self._total_edges - 1)
        for vertex, vertex_edges in self._graph.items():
            if len(vertex_edges) <= rand_edge:
                rand_edge -= len(vertex_edges)
            else:
                from_vertex = vertex
                to_vertex = vertex_edges[rand_edge]
                return from_vertex, to_vertex
        


if __name__ == '__main__':
    i= 0
    count = 10000
    final_edge=0
    while i < 100:
        data = KargerMinCutter('data.txt')
        min_cut = data.find_min_cut()
        if min_cut < count:
            count  = min_cut
            final_edge = edge
        i=i+1


