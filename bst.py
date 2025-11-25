# bst.py
# An implementation of a binary search tree
# Modified by:
# Please try to write this yourself without using an LLM.



class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    #Insert value in BSN 
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            self.count += 1
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(value)
                    break
                current = current.right

        self.count += 1

    # return the number of nodes in the BST
    def __len__(self):
        return self.count

    # check if a value is in the BST using: value in bst
    def __contains__(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    # return list of values in ascending order
    def in_order_walk(self):
        result = []
        self.in_order_walk_helper(self.root, result)
        return result

    def in_order_walk_helper(self, current, accumulated):
        if current is None:
            return

        self.in_order_walk_helper(current.left, accumulated)
        accumulated.append(current.value)
        self.in_order_walk_helper(current.right, accumulated)

    def minimum(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value

    def maximum(self):
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        return current.value

    
    
