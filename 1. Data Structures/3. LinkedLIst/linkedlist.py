# Linked List A linked list is a data structure that consists of a
# sequence of elements, where each element (node) contains a 
# reference (or link) to the next node in the sequence.
# This allows for efficient insertion and deletion of elements.

# Node Class

class Node:
    def __init__(self, value):
        self.value = value # Store the data
        self.next = None # Initialize the pointer to None

class LinkedList:
    def __init__(self):
        self.head = None # Initialize the head of the list
    
    def append(self, value):
        new_node = Node(value)
        if not self.head: # if the list is empty
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next: # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node # Link the new node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" --> ")
            current_node = current_node.next
        print("None")

# # Example Usage:
# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(3)
#     ll.append(6)
#     ll.append(9)
#     ll.display()


# Insertion at the Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head # Link the new node to the current head
        self.head = new_node # Update the head to the new node
    
# Deletion
    def delete_node(self, key):
        current_node = self.head 
        
        # if the head node itself hold the key
        if current_node and current_node.value == key:
            self.head = current_node.next # change head
            current_node = None # Free the memory garbage collection
            return 
        
        # Search for the key to be deleted
        prev_node = None
        while current_node and current_node.next != key:
            prev_node = current_node
            current_node = current_node.next 
        
        # if the key not present in the list
        if not current_node:
            return 
        
        # unlink the node from the ll 
        prev_node.next = current_node.next 
        current_node = None
        
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.value == key:
                return True
            current_node = current_node.next 
        return False

#Usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(6)
    ll.append(9)
    ll.display()
    
    ll.insert_at_beginning(3)
    ll.display()
    
    ll.delete_node(3)
    ll.display()
    
    print(ll.search(9))
    print(ll.search(4))
    