class BinaryTreeNode(object):
    root = None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        pass

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

    @classmethod
    def create_tree(cls, iterable):
        iterable = iterable.copy()
        cls.root = BinaryTreeNode(iterable.pop())

        for element in range(len(iterable)):
            cls.root.insert(iterable.pop(), cls.root)
        return cls

    @staticmethod
    def insert(value, node):
        if node.left is None:
            node.left = BinaryTreeNode(value)

        elif node.right is None:
            node.right = BinaryTreeNode(value)

        elif value < node.right:
            return node.insert(value, node.left)

        else:
            return node.insert(value, node.right)

    def search_recursively(self, value, node):
        if value is None or value is self.value:
            return node
        if value <= self.left:
            return self.search_recursively(value, self.left)
        if value > self.right:
            return self.search_recursively(value, self.right)