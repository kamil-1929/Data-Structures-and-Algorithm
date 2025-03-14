# Binary Search Tree (BST)
# A binary search tree is a binary tree with the additional property 
# that for each node, all values in the left subtree are less than 
# the node's value, and all values in the right subtree are greater than 
# or equal to the node's value.

    #     10
    #    /  \
    #   5    15
    #  / \   / \
    # 3   8 12  20
    
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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursively(self.root, value)
        
    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursively(node.right, value)
    
    def inorder_traverse(self):
        return self._inorder_recursively(self.root)
    
    def _inorder_recursively(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursively(node.left))
            result.append(node.value)
            result.extend(self._inorder_recursively(node.right))
        return result

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(33)
    bst.insert(36)
    bst.insert(45)
    bst.insert(6)
    bst.insert(23)
    bst.insert(24)
    bst.insert(25)
    bst.insert(26)
    bst.insert(9)
    bst.insert(10)
    bst.insert(14)
    bst.insert(15)
    bst.insert(19)
    
    print("Inorder Traversal", bst.inorder_traverse())
     
