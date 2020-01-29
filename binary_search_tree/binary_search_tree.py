from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If input value is less than root/current value (self.value)...
        if value < self.value:
            # Assuming there's nothing on the left side (self.left)...
            if self.left is None:
                # Assign a new BST(value) to self.left
                self.left = BinarySearchTree(value)
            else:
                # Otherwise (not empty), call this method on self.left -- going through the logic again = how value arg lands in the correct order
                self.left.insert(value)
        # If input value is greater than root/current value (self.value)...
        else:
            # Assuming there's nothing on the right side (self.right)...
            if self.right is None:
                # Assign a new BST(value) to self.right
                self.right = BinarySearchTree(value)
            else:
                # Otherwise (not empty), call this method again on self.right -- same reasoning as ^^^
                self.right.insert(value)

    # Return True if the tree contains the value or False if it does not
    def contains(self, target):
        # If target (input value) *equals* root/current value (self.value)...
        if target == self.value:
            # Return True
            return True
        # If target is less than root/current value...
        if target < self.value:
            # If there's nothing on the left...
            if not self.left:
                # Return False (input doesn't exist)
                return False
            else:
                # Otherwise (stuff on left), return + call this method again on self.left -- gotta repeat same logic until target == value or False
                return self.left.contains(target)
        # If target is greater than root/current value...
        if target > self.value:
            # If there's nothing on the right...
            if not self.right:
                # Return False (input doesn't exist)
                return False
            else:
                # Otherwise (stuff on right), return + call this method again on self.right -- ^^^ ditto
                return self.right.contains(target)
        # No else necessary here because it's impossible for an input to not eventually hit one of the above functional criteria

    # Return the maximum value found in the tree
    def get_max(self):
        # If there's anything on the right (where bigger elements live)...
        if self.right:
            # Return + call this method on self.right until the max is located
            return self.right.get_max()
        else:
            # Otherwise, return root/current value (self.value) because there are no larger numbers
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Call cb and pass in root/current value (self.value)
        cb(self.value)
        # If there are elements on the right...
        if self.right:
            # Call *this* method on all of them and pass the callback function in as an argument
            self.right.for_each(cb)
        # If there are elements on the left...
        if self.left:
            # Call *this* method on all of them and pass cb in as an argument
            self.left.for_each(cb)
        else:
            # Otherwise, the work is done, so you can simply return
            return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
