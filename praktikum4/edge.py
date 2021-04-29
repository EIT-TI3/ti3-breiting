# (c) 2021 Yannic Breiting


class Edge:
    def __init__(self, name, weight):
        self._name = name
        self.weight = weight
        self._next = None

    def connect(self, n):
        self._next = n

    def get_connect(self):
        return self._next

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'{self._name}/{self.weight}'

