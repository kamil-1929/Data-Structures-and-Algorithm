# Simple Queue Implementation:
# Array Queue is bad because of the memory space complexity  due to reindexing

# Big O of LinkedList Queue:
# Lookup O(n)
# Enqueue O(1)
# Dequeue O(1)
# Peek O(1)


class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(9)
    print("Dequeued Item:", queue.dequeue())
    print("Peek Item", queue.peek())
    print("Size of the Queue:", queue.size())

# Queue Using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedListQueue:
    def __init__(self):
        self.front = None 
        self.rear = None 
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.front.value
    
    def get_size(self):
        return self.size

if __name__ == "__main__":
    ll_queue = LinkedListQueue()
    ll_queue.enqueue(3)
    ll_queue.enqueue(6)
    ll_queue.enqueue(9)
    print(ll_queue.dequeue())
    print(ll_queue.peek())
    print(ll_queue.get_size())
    