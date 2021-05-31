import heapq
import itertools


class NodeHeap:
    REMOVED = '<removed-task>'  # placeholder for a removed task
    counter = itertools.count()  # unique sequence count

    def __init__(self):
        self.heap = []
        self.entries = {}

    def __len__(self):
        return len(self.heap)

    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task in self.entries:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entries[task] = entry
        heapq.heappush(self.heap, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entries.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task is not self.REMOVED:
                del self.entries[task]
                return task
        raise KeyError('pop from an empty priority queue')
