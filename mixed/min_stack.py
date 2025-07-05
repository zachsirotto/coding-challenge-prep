# Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self): return self.stack[-1]
    def get_min(self): return self.min_stack[-1]
