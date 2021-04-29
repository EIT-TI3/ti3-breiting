# (c) 2021 Yannic Breiting


class Node:
    _id = 0

    def __init__(self, name):
        self.name = name
        self.next = []

    def __str__(self):
        output = f"{self.name}"
        if len(self.next) != 0:
            for idx, node in enumerate(self.next):
                if idx != 0:
                    output += " "
                output += f" ---> {node.name}\n"
            output = output[:-1]
        elif len(self.next) == 0:
            output += " <end>"

        return output


if __name__ == '__main__':
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n1.next.append(n2)
    n1.next.append(n3)
    print(n3.name)
    print(n1)
    print(n2)
