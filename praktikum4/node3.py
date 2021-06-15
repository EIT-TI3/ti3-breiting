
# (c) 2021 Yannic Breiting


class Node:
    __id = 0

    def __init__(self, name=None):
        Node.__id += 1
        self.__next = []

        if name is None:
            self.__name = f'Knoten {Node.__id}'
        else:
            self.__name = name

    def __str__(self):
        output = f"{self.__name}"
        if len(self.__next) != 0:
            for idx, node in enumerate(self.__next):
                if idx != 0:
                    output += " " * len(self.__name)
                output += f" ---> {node.name}\n"
            output = output[:-1]
        else:
            output += " <end>"

        return output

    @property
    def name(self):
        return self.__name

    def connect(self, n):
        self.__next.append(n)

    def get_connects(self):
        return tuple(self.__next)


if __name__ == '__main__':
    n1 = Node()
    n2 = Node('B')
    n3 = Node()
    n1.connect(n2)
    n1.connect(n3)
    print(n1)
    print(n2)
