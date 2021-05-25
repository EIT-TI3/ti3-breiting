# (c) 2021 Yannic Breiting


class Edge:
    def __init__(self, name, weight):
        self.__name = name
        self.weight = weight
        self.__next = None

    def connect(self, n):
        self.__next = n

    def get_connect(self):
        return self.__next

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'{self.__name}/{self.weight}'

