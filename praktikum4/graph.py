from node import Node
from edge import Edge


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.queue = []

    def new_node(self, name=None) -> Node:
        node = Node(name)
        self.nodes.update({node.name: node})
        return node

    def new_edge(self, name, weight) -> Edge:
        edge = Edge(name, weight)
        self.edges.update({edge.name: edge})
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
            except:
                output = -1
                break
            n1 = n2

        return output

    @staticmethod
    def find_edge_between(n1, n2, weight=True):
        connecting_node = set(n1.neighbours()) & {n2}
        if len(connecting_node) != 0:
            for edge in n1.get_connects():
                if edge.get_connect() is n2:
                    return edge.weight if weight else edge

    def _initialize_dijkstra(self, start_node):
        start_node.distance = 0

        for node in self.nodes.values():
            node.distance = float('inf')
            node.predecessor = None

            if start_node in node.neighbours():
                node.distance = self.find_edge_between(start_node, node)

            self.queue.append((node.distance, node))

    def dijkstra(self, start_node, end_node):
        start_node, end_node = self.find_node(start_node), self.find_node(end_node)
        self._initialize_dijkstra(start_node)

        while len(self.queue) > 0:
            node = self.shortest_node()[1]

            for neighbour in node.neighbours():
                if neighbour in (element[1] for element in self.queue):
                    self.update_distance(node, neighbour)

            if end_node.predecessor is not None:
                print(*self.create_shortest_path(end_node, start_node))
                print(end_node.distance)
                break

    def shortest_node(self):
        length, node_idx = float('inf'), None

        for idx, element in enumerate(self.queue):
            if element[0] < length:
                length = element[0]
                node_idx = idx

        return self.queue.pop(node_idx)

    def update_distance(self, node, neighbour):
        new_distance = self.path_length([node, neighbour]) + node.distance

        if new_distance < neighbour.distance:
            neighbour.distance = new_distance
            neighbour.predecessor = node
            self.update_queue(neighbour)

    def update_queue(self, node):
        for idx, element in enumerate(self.queue):
            if element[1] == node:
                self.queue[idx] = (node.distance, node)

    def create_shortest_path(self, end_node, start_node):
        predecessor = end_node
        path = []

        while predecessor is not None:
            if predecessor.predecessor is not None:
                path.append(f'\n{self.find_edge_between(predecessor, predecessor.predecessor, weight=False).name} '
                            f'--> {predecessor.name}')
            predecessor = predecessor.predecessor

        path.append(start_node.name)

        return path[::-1]
