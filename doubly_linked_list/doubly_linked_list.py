"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            # current_next = hint the insert is after
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            # current_prev = hint the insert is before
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        # Necessary because deleting changes other node's next/previous
        if self.prev:
            # Rearrange previous "next" pointer to this node's
            self.prev.next = self.next
        if self.next:
            # Rearrange next "previous" pointer to this node's
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        # Default is none just in case no nodes exist
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        # This method is often expected in the workplace
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
        # Automatically head/tail if no other nodes
            self.head = new_node
            self.tail = new_node
        else:
        # Otherwise we have to rearrange the pointers
            new_node.next = self.head
            # Current head becomes new node's "next"
            self.head.prev = new_node
            # Current head's "previous" becomes new node
            self.head = new_node
            # Now it's safe to assign new node as new head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        # Value is here because it's explicitly requested in return
        self.delete(self.head)
        # Can simply use the delete method already created above
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
        # Otherwise we need to rearrange the pointers
            new_node.prev = self.tail
            # Current tail becomes new node's "previous"
            self.tail.next = new_node
            # Current tail's "next" becomes the new node
            self.tail = new_node
            # Now it's safe to assign new node as new tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        # Don't have to reassign pointers - already done by delete()
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # Need value so we have something to assign
        value = node.value
        # Remove node from current spot, reassign pointers
        self.delete(node)
        # Add node to the head, reassign those pointers too
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Need value so we have something to assign
        value = node.value
        # Remove node from current position, modify pointers
        self.delete(node)
        # Add node to the tail, edit those pointers as well
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Decrement length to fit deletion
        self.length -= 1

        # LL is empty
        if not self.head and not self.tail:
            # Nothing to delete, so just return
            return
        
        # If head and tail are the same
        if self.head == self.tail:
            # Assign both values to None
            self.head = None
            self.tail = None

        # If node is the head
        elif self.head == node:
            # Next element automatically becomes new head
            self.head == self.head.next
            node.delete()

        # If node is the tail
        elif self.tail == node:
            # Previous element automatically becomes new tail
            self.tail == self.tail.prev
            node.delete()

        # Otherwise
        else:
            # Existing delete method handles the pointers
            node.delete()
            # (It changes assignment to self.next and self.prev)
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # If there's no head, there can't possibly be a max
        if self.head is None:
            return None
        # Otherwise, we can assume max value is in front
        max_value = self.head.value
        # Create placeholder variable for comparison
        current = self.head
        # While max value doesn't match self.head
        while current:
            # Reassign max if current is bigger
            if current.value > max_value:
                max_value = current.value
            # Increment by calling next on CV
            current = current.next
        # After loop is complete, return max
        return max_value
