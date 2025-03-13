# Basic Stack Implementation

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def is_empty(self):
        return len(self.items) == 0

# Using the stack
stack = Stack()
stack.push(3)
stack.push(6)
stack.push(9)
print("Popped Item", stack.pop())
print("Popped Item", stack.pop())
print("Popped Item", stack.pop())