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
        output = self.__name
        if len(self.__next) > 0:
            for idx, edge in enumerate(self.__next):
                if idx != 0:
                    output += " " * len(self.__name)
                output += f" --{edge}--> {edge.get_connect().name}\n"
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

    def neighbours(self):
        for edge in self.__next:
            yield edge.get_connect()
