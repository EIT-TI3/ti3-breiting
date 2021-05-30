import itertools
from math import floor
import heapq


def slowsort(iterable, *_args):
    if _args is None:
        i, j = min(iterable), max(iterable)
    else:
        i, j = _args

    if i < j:
        m = floor((i + j) / 2)

        slowsort(iterable, i, m)
        slowsort(iterable, m + 1, j)

        if iterable[j] < iterable[m]:
            iterable[j], iterable[m] = iterable[m], iterable[j]

        slowsort(iterable, i, j - 1)

    return


class BinaryTree(object):
    root = None

    @classmethod
    def create_tree(cls, iterable):
        iterable = iterable.copy()
        cls.root = BinaryTreeNode(iterable.pop())

        for element in range(len(iterable)):
            cls.root.insert(iterable.pop(), cls.root)
        return cls

    def search_recursively(self, value, node):
        if value is None or value is node:
            return value
        if value <= node.left:
            return self.search_recursively(value, node.left)
        if value > node.right:
            return self.search_recursively(value, node.right)


class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __ge__(self, other):
        return self.value >= other

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


class NodeHeap:
    REMOVED = '<removed-task>'  # placeholder for a removed task
    counter = itertools.count()  # unique sequence count

    def __init__(self):
        self.heap = []
        self.entries = {}

    def __len__(self):
        return len(self.heap)

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entries:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entries[task] = entry
        heapq.heappush(self.heap, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entries.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task is not self.REMOVED:
                del self.entries[task]
                return task
        raise KeyError('pop from an empty priority queue')
