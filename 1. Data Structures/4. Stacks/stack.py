
# Big (O) - Both Stack and Link is fine for the Stack due to same complexity
# Linked List
# Lookup O(n)
# push = O(1)
# pop = O(1)
# peek = O(1)

# Simple Stack using a list in Python 
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError(" Pop from an empty stack")            
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1] 
    
    def size(self):
        return len(self.items)

# if __name__ == "__main__":
#     # Using the stack
#     stack = Stack()
#     stack.push(3)
#     stack.push(6)
#     stack.push(9)
#     stack.push(10)
#     print("Popped Item", stack.pop())
#     print("Peek Item", stack.peek())
#     print("Size of the stack", stack.size())
    
# Stack Using LinkedList 
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
    
class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return IndexError("Pop from an Empty Stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty Stack")
        return self.top.value
    
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next 
        return count 

if __name__ == "__main__":
    ll_stack = LinkedListStack()
    ll_stack.push(3)
    ll_stack.push(6)
    ll_stack.push(9)
    print("Popped item :", ll_stack.pop())
    print("Peek Item :", ll_stack.peek())
    print("Size of the stack :", ll_stack.size())
    