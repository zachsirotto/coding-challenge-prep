# Stack implementation
class Stack:
    def __init__(self):
        self.container = []
    def push(self, item): self.container.append(item)
    def pop(self): return self.container.pop()
    def peek(self): return self.container[-1]
    def is_empty(self): return not self.container
