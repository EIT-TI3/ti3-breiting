# (c) 2021 Yannic Breiting


class Node:
    _id = 0

    def __init__(self, name=None):
        self._id = self.incr()
        self._next = []

        if name is None:
            self._name = f'Knoten {self._id}'
        else:
            self._name = name

    def __str__(self):
        output = f"{self._name}"
        if len(self._next) > 0:
            for idx, edge in enumerate(self._next):
                if idx != 0:
                    output += " " * len(self._name)
                output += f" --{edge}--> {edge.get_connect().name}\n"
            output = output[:-1]
        else:
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
