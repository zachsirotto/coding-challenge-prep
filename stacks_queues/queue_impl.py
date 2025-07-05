# Queue implementation
from collections import deque
class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self, item): self.container.append(item)
    def dequeue(self): return self.container.popleft()
    def is_empty(self): return not self.container
