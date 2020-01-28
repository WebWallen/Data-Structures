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
        # Now the DLL and self.storage are two separate entities, hence self.list
        self.list = DoublyLinkedList()
        # Self.storage should be a dictionary since it allows for key/value pairs
        self.storage = dict()
        # Limit is here to make sure we don't need to make room for new data
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the key isn't stored, there's nothing to return
        if key not in self.storage:
            return None
        # Otherwise, assign the key value to node variable
        node = self.storage[key]
        # Most recently accessed so move node to the front
        self.list.move_to_front(node)
        # Add [1] because otherwise returns two entities
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
        # If key is already stored, simply update its value
            node = self.storage[key]
            # Most recently accessed so move to the front
            self.list.move_to_front(node)
            # Assign a tuple to node for key and value
            node.value = (key, value)
            # Return the new value of existing key
            return node.value

        if len(self.list) >= self.limit:
        # If we're at max capacity, remove least recently used item (tail)
            self.storage.pop(self.list.tail.value[0])
            # Removes key from the dictionary
            self.list.remove_from_tail()
            # Removes value from the DLL
        
        # Add the key/value pair to the head since it's most recently used
        self.list.add_to_head((key, value))
        # Key of dictionary should coincide with value of the DLL
        self.storage[key] = self.list.head
        # Return the newly created, most recently used item
        return self.list.head