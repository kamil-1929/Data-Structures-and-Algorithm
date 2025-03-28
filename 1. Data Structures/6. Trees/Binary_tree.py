# Basic Binary Tree Implementation
# A binary tree is a tree data structure in which each node has at most 
# two children, referred to as the left child and the right child.

    #     10
    #    /  \
    #   20   30
    #  / \   / \
    # 40  50 60  70
#     Key Differences
# Ordering:
# Binary Tree: No specific ordering of nodes.
# Binary Search Tree: Follows the left < parent < right rule.

# Searching:
# Binary Tree: Searching for a value may require traversing the entire tree.
# Binary Search Tree: Searching is efficient due to the ordering, allowing for O(log n) time complexity on average.

# Insertion and Deletion:
# Binary Tree: Insertion can be done in any order without regard for value.
# Binary Search Tree: Insertion and deletion must maintain the BST properties.


class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None # Initialize the root of the tree
        
    def insert(self, value):
        """Insert method"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        """Helper method to insert a new node recursively."""
        if node.left is None:
            node.left = Node(value)
        elif node.right is None:
            node.right = Node(value)
        else:
            self._insert_recursively(node.left, value)
    
    def inorder_traversal(self):
        return self._inorder_recursively(self.root)
    
    def _inorder_recursively(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursively(node.left)) # Visit left subtree
            result.append(node.value) # Visit Node
            result.extend(self._inorder_recursively(node.right)) # Visit Right
        return result

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(3)
    bt.insert(33)
    bt.insert(36)
    bt.insert(45)
    bt.insert(6)
    bt.insert(23)
    bt.insert(24)
    bt.insert(25)
    bt.insert(26)
    bt.insert(9)
    bt.insert(10)
    bt.insert(14)
    bt.insert(15)
    bt.insert(19)
   

    print("Inorder Traversal", bt.inorder_traversal())
    
                            