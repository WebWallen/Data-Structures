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
        # If there's actually a value...
        if self.value is not None:
            # If there are any elements on the left...
            if self.left:
                # Recursively call this function on the left branch
                self.left.in_order_print(self.left) # First self.left is the next branch and the second is its twigs/leaves
            # Print value -- they end up in order since it goes: root/current -> left branch -> left-right -> right branch -> right-left -> right-right
            print(self.value)
            # If there are any elements on the right...
            if self.right:
                # Recursively call this function on the right branch
                self.right.in_order_print(self.right) # First self.right is the next branch and the second is its twigs/leaves

    # Print the value of every node, starting with the given node, in an iterative breadth first traversal (breadth first means "USE A QUEUE")
    def bft_print(self, node):
        # If there's not a node value, there's nothing to do, so simply return
        if node.value is None:
            return
        # Assign an empty Queue class to a queue variable (this is possible due to the imports on top)
        queue = Queue()
        # Call enqueue on the queue to add a node(argument) to the back of our line
        queue.enqueue(node)
        # While the queue has a length... (note: wouldn't work with typical len(check_me) syntax -- don't know why, but use check_me.len() instead)
        while queue.len() is not 0:
            # Call dequeue on the queue to remove a node from the front of our line and assign it to a "leaf" variable
            leaf = queue.dequeue()
            # Print the leaf's value
            print(leaf.value)
            # If there are anymore leaves on the left side...
            if leaf.left is not None:
                # Call enqueue on the queue and pass those leaves in as an argument
                queue.enqueue(leaf.left)
            # If there are anymore leaves on the right side...
            if leaf.right is not None:
                # Call enqueue on the queue and pass those leaves in as an argument
                queue.enqueue(leaf.right)

    # Print the value of every node, starting with the given node, in an iterative depth first traversal (depth first means "USE A STACK")
    def dft_print(self, node):
        # If there's not a node value, there's no work to do, so simply return
        if node.value is None:
            return
        # Create an empty Stack() and assign it to a "stack" variable
        stack = Stack()
        # Call the push method on "stack" and pass in the node as an argument
        stack.push(node)
        # While the stack has a length (see note in queue about the dot notation versus parenthesis as usual)
        while stack.len() is not 0:
            # Call the pop method on "stack" and assign the result to an element variable
            element = stack.pop()
            # Print the element's value
            print(element.value)
            # If there are any elements on the left...
            if element.left is not None:
                # Call the push method on "stack" and pass the left element inside
                stack.push(element.left)
            # If there are any elements on the right...
            if element.right is not None:
                # Call the push method on "stack" and pass the right element inside
                stack.push(element.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
