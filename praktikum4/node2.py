# (c) 2021 Yannic Breiting


class Node:
    __id = 0

    def __init__(self, name):
        self.__name = name
        self.next = []

    def __str__(self):
        output = f"{self.__name}"
        if len(self.next) != 0:
            for idx, node in enumerate(self.next):
                if idx != 0:
                    output += " "
                output += f" ---> {node.name}\n"
            output = output[:-1]
        elif len(self.next) == 0:
            output += " <end>"

        return output

    @property
    def name(self):
        return self.__name


if __name__ == '__main__':
    n1 = Node('A')
    print(n1.name)
