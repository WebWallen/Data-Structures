from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Now the DLL and self.storage are two separate entities, hence self.list as home for DoublyLinkedList()
        self.list = DoublyLinkedList()
        # Self.storage should be assigned an empty dictionary since it needs to store key/value pairs
        self.storage = dict()
        # Limit is here to make sure we don't need to make room for new data -- assign to self.limit
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the key isn't in self.storage, there's nothing to return (0)
        if key not in self.storage:
            return None
        # Otherwise, assign the storage [key] value to node variable
        node = self.storage[key]
        # Most recently accessed node so move it to the front
        self.list.move_to_front(node)
        # return node value [1] (because it's a key/VALUE)
        return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
        # If key is already stored, simply update key contained in storage
            node = self.storage[key]
            # Most recently accessed so move to the front of DLL (list)  
            self.list.move_to_front(node)
            # Assign both the (key, and, value) to node.value
            node.value = (key, value)
            # Return the the key value pair inside node.value
            return node.value

        if len(self.list) >= self.limit:
        # If we're at max capacity, remove key value [0] of the DLL's tail from storage with pop
            self.storage.pop(self.list.tail.value[0])
            # Remove the DLL node from tail
            self.list.remove_from_tail()
        
        # Add the destructured key and value to head since it's most recently used
        self.list.add_to_head((key, value))
        # Update [key] of storage dictionary to match the head of our DLL
        self.storage[key] = self.list.head
        # Return the newly created, most recently used node (DLL head)
        return self.list.head