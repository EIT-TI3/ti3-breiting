# (c) 2021 Yannic Breiting


class Node:
    __id = 0

    def __init__(self, name=None):
        self.__id = self.incr()
        self.__next = []
        self.distance = float('inf')
        self.predecessor = None

        if name is None:
            self._name = f'Knoten {self.__id}'
        else:
            self._name = name

    def __str__(self):
        output = f"{self._name}"
        if len(self.__next) > 0:
            for idx, edge in enumerate(self.__next):
                if idx != 0:
                    output += " " * len(self._name)
                output += f" --{edge}--> {edge.get_connect().name}\n"
            output = output[:-1]
        else:
            output += " <end>"
        return output

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    @classmethod
    def incr(cls):
        cls.__id += 1
        return cls.__id

    @property
    def name(self):
        return self._name

    def connect(self, n):
        self.__next.append(n)

    def get_connects(self):
        return tuple(self.__next)

    def neighbours(self):
        for edge in self.__next:
            yield edge.get_connect()
