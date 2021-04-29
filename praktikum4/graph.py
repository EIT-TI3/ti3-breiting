from collections import Counter

from node import Node
from edge import Edge


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def new_node(self, name=None) -> Node:
        node = Node(name)
        self.nodes.append(node)
        return node

    def new_edge(self, name, weight) -> Edge:
        edge = Edge(name, weight)
        self.edges.append(edge)
        return edge

    def find_node(self, name) -> Node:
        try:
            output = next(self.find_name(self.nodes, name))
        except StopIteration:
            output = None
        return output

    def find_edge(self, name) -> Edge:
        try:
            output = next(self.find_name(self.edges, name))
        except StopIteration:
            output = None
        return output

    @staticmethod
    def find_name(iterable, name):
        for i in iterable:
            if i.name == name:
                yield i

    def __str__(self):
        output = 'Knoten:\n' \
                 '-------\n'
        for node in self.nodes:
            output += str(node) + '\n'

        output += '\nKanten:\n' \
                  '-------\n'

        for edge in self.edges:
            output += str(edge) + '\n'

        return output

    def path_length(self, path_node_names):
        output = 0
        n1 = path_node_names.pop(0)
        for n2 in path_node_names:
            try:
                output += self.find_edge_between(self.find_node(n1), self.find_node(n2))
            except:
                output = -1
                break
            n1 = n2
        return output

    # TODO: Haut noch nicht FEHLER
    @staticmethod
    def find_edge_between(n1, n2):
        return Counter(list(yield_connections(n1)) + list(yield_connections(n2))).values()


def yield_connections(n):
    for edges in n.get_connects():
        yield edges.get_connect()


if __name__ == '__main__':
    Node._Node__id = 0
    g = Graph()
    A = g.new_node('A')
    B = g.new_node('B')
    C = g.new_node('C')
    D = g.new_node('D')
    E = g.new_node('E')
    F = g.new_node('F')
    a = g.new_edge('a', 3)
    a.connect(B)
    b = g.new_edge('b', 7)
    b.connect(C)
    c = g.new_edge('c', 5)
    c.connect(D)
    d = g.new_edge('d', 4)
    d.connect(E)
    e = g.new_edge('e', 2)
    e.connect(A)
    f = g.new_edge('f', 1)
    f.connect(B)
    A.connect(a)
    B.connect(b)
    C.connect(c)
    C.connect(d)
    D.connect(e)
    F.connect(f)
    g.path_length(["A", "B", "C", "D", "A"])
