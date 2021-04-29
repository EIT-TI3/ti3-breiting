# (c) 2021 Yannic Breiting


class Node:
    _id = 0

    def __init__(self, name):
        self._name = name
        self.next = []

    def __str__(self):
        output = f"{self._name}"
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
        return self._name


if __name__ == '__main__':
    n1 = Node('A')
    print(n1.name)
