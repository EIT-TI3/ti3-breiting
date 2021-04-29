# (c) 2021 Yannic Breiting


class Node:
    _id = 0

    def __init__(self, name=None):
        self.id = self.incr()
        self._next = []

        if name is None:
            self._name = f'Knoten {self.id}'
        else:
            self._name = name

    def __str__(self):
        output = f"{self._name}"
        if len(self._next) != 0:
            for idx, node in enumerate(self._next):
                if idx != 0:
                    output += " " * len(self._name)
                output += f" ---> {node.name}\n"
            output = output[:-1]
        elif len(self._next) == 0:
            output += " <end>"

        return output

    @classmethod
    def incr(cls):
        cls._id += 1
        return cls._id

    @property
    def name(self):
        return self._name

    def connect(self, n):
        self._next.append(n)

    def get_connects(self):
        return tuple(self._next)


if __name__ == '__main__':
    n1 = Node()
    n2 = Node('B')
    n3 = Node()
    n1.connect(n2)
    n1.connect(n3)
    print(n1)
    print(n2)
