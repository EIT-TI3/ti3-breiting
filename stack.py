class Stack:
    def __init__(self):
        self.l = []

    def push(self, o):
        self.l.append(o)

    def pop(self):
        return self.l.pop()

    def size(self):
        return len(self.l)

    def isEmpty(self):
        return len(self.l) == 0

    def top(self):
        return self.l[-1]