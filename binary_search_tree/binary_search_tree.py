  
# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

from queue import Queue

from stack import Stack


"""

1024 ==> 2 ^ 10
512
256
128
64   ==> 2^6
32
16   ==> 2^4
8    ==> 2^3
4
2
1

exponets til how many step to take

O(log n)


Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# node = BSTNode(1)

# node_3_who_is_right_child

# node.insert(2)
# node.insert(3)

#node. insert(0)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if gte, got right!
        if value >= self.value:
            #check if .right exists
            if self.right is not None:
            ## if so, make that node call insert with the same value
                self.right.insert(value)

            ## if not, create a node with that value, set node as right child
            else:
                new_node = BSTNode(value)
                self.right = new_node
                # or this
                self.right = BSTNode(value)
        # else, go left!
        else:
            # check if .left exists
            if self.left is not None:
            # if so, make that node call insert with the same value
                self.left.insert(value)
            ## if not, create a node right here
            else:
                new_node = BSTNode(value)
                self.left = new_node
        
        """
        # self wil be the root
        # compare value to the current node 
        # if no node to go to, (either left or right)
            # make the new node at that spot
        while True:
        # compare value to the current node 
        # if smaller, go left
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                    return self.left
                else:
                    self = self.left
            # if bigger, go right_rotate
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                    return self.right
                else:
                    self = self.right
        """

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

        else:
            if self.left is not None: # we have a left child
                return self.left.contains(target) # hand the target off teh left child
            else:
                return False

        """
        while True:
            # if equal return True
            if self.value == target:
                return True
            # check right
            if target > self.value:
                if self.right is None:
                    return False
                else:
                    self = self.right
            # check left
            elif target < self.value:
                if self.left is None:
                    return False
                else:
                    self = self.left
        """            

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    """
        def get_max(self):
            if self.right:
                return self.right.get_max()
            else:
                return self.value
    """

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)


        if self.right:
            self.right.for_each(fn)

    # refers to the order of operations.
    #preorder
    #inorder
    #postorder

    # node_10 = BSTNode(10)
    # node_10.for_each(print)

    # 10, 8, 7, 9, 12, 11, 13
    # Part 2 -----------------------

    # Travserval - 
    # Search - search and stop at 

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

        # make queue
        # enqueue the node
        # as long as the queue is not empty
        ## dequeue from the front of the queue, this is our current node
        ## enqueue the kids of the current node on the stack

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

        # make a stack
        # push the node on the statck
        # as long as the stack is not empty
        ## pop off the stack, this is our current node
        ## put the kids of  the current node on the stack 
        ## (check that they are not None, then put them on the stack)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
