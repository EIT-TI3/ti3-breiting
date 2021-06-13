from algorithms.heap import NodeHeap

from node import Node
from edge import Edge


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.heap = NodeHeap()

    def __str__(self):
        output = 'Knoten:\n' \
                 '-------\n'
        for node in self.nodes.values():
            output += str(node) + '\n'

        output += '\nKanten:\n' \
                  '-------\n'

        for edge in self.edges.values():
            output += str(edge) + '\n'

        return output

    def new_node(self, name=None) -> Node:
        node = Node(name)
        self.nodes[node.name] = node
        return node

    def new_edge(self, name, weight) -> Edge:
        edge = Edge(name, weight)
        self.edges[edge.name] = edge
        return edge

    def find_node(self, name) -> Node:
        try:
            output = self.nodes[name]
        except KeyError:
            output = None
        return output

    def find_edge(self, name) -> Edge:
        try:
            output = self.edges[name]
        except KeyError:
            output = None
        return output

    def path_length(self, path_node_names):
        output = 0
        n1 = path_node_names.pop(0)

        if isinstance(n1, str):
            n1 = self.find_node(n1)

        for n2 in path_node_names:
            if isinstance(n2, str):
                n2 = self.find_node(n2)
            try:
                output += self.find_edge_between(n1, n2)
            except TypeError:
                output = -1
                break
            n1 = n2

        return output

    @staticmethod
    def find_edge_between(n1, n2, weight=True):
        for edge in n1.get_connects():
            if edge.get_connect() is n2:
                return edge.weight if weight else edge

    def dijkstra(self, start_node, end_node):
        start_node, end_node = self.find_node(start_node), self.find_node(end_node)

        self._initialize_dijkstra(start_node)

        while len(self.heap) > 0:
            node = self.heap.pop_task()

            for neighbour in node.neighbours():
                self._update_distance(node, neighbour)

            if end_node.predecessor is not None:
                self._create_shortest_path(end_node)
                break

    def _initialize_dijkstra(self, start_node):
        for node in self.nodes.values():
            node.distance = float('inf')
            node.predecessor = None

            if node is start_node:
                start_node.distance = 0

            self.heap.add_task(node, priority=node.distance)

    def _update_distance(self, node, neighbour):
        new_distance = self.find_edge_between(node, neighbour) + node.distance

        if new_distance < neighbour.distance:
            neighbour.distance = new_distance
            neighbour.predecessor = node
            self.heap.remove_task(neighbour)
            self.heap.add_task(neighbour, priority=neighbour.distance)

    def _create_shortest_path(self, end_node):
        predecessor = end_node
        path = 0
        way = [f'{end_node.name}\n']

        while predecessor.predecessor is not None:
            edge = self.find_edge_between(predecessor, predecessor.predecessor, weight=False)
            way.append(f'{predecessor.predecessor.name} --> {edge}\n')

            path += edge.weight
            predecessor = predecessor.predecessor

        print(*reversed(way))
        print(f'Länge des Weges: {path}')
