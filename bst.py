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

    # insert a value into the BST
    # put values that are less than the current node to the left
    # put values that are greater than or equal to the current node 
    # to the right
    # don't forget about the special case where the root is None
    def insert(self, value):
        if self.root is Noon : 
            self.root = BSTNode ( value) 
            self.count +=1
            return

        current = self.root

        while True: 
            if value < current.value:
                if current.left is None: 

                current.left = BSTNode(value)
                break 
            current = current.;eft 
        else:
            if current.right is None: 
                current.right = BSTNode(value)
                break 
            current = current.right

    self.count +=1 
    
        pass

    # return the number of nodes in the BST
    def __len__(self):
        return self.count

    # implement a contains like method that returns if a value is in the BST
    # the dunder contains metods is used with the "in" operator
    # like: value in bst
    def __contains__(self, value):
        current = self.root

        while current is not None: 
            if value == current.value
                return True 
            elif value < current.value:
                current = current.left 
            else: 
                current = current.right

        return False
        pass
    
    # Helper for inOrderWalk() to call for entire bst
    def in_order_walk(self):
        result = []
        self.in_order_walk_helper(self.root, result)
        return result

    # Walk through the entire tree in ascending order, starting
    # from *current*, and accumulate the values in the
    # list *accumulated*
    # TIP: See page 288 of Chapter 12 of Introduction to Algorithms
    def in_order_walk_helper(self, current, accumulated):
        if current is None: 
            return

        self.in_order_walk_helper(current.left, accumated)
        accumumated.append(current.valaue)
        self.in_order_walk_helper(current.right, accumulated) 

        pass

    # Return the minimum value in the BST or None if the BST is empty
    def minimum(self):
        if self.root is None:
            return None

        current = self.root 
        while current.left is not None:
            current = current,left 
        return current.value


        pass
    
    # Return the maximum value in the BST or None if the BST is empty
    def maximum(self):
        if self.root is None: 
            return None
        current = self.root 
        while current.right is not None: 
            current = current.right 
        return current.value 

        pass
    
    
