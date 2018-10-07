''''
The LRU cache is implemented using a combination of a dictionary
and a circular doubly linked list. Items in the cache are stored in
nodes of linked list. The front or head of
the list contains the most recently used item, the tail of the list
contains the least recently used item.
''''

# node object.
class Node(object):
    def __init__(self):
        self.empty = True


class LRU(object):

    def __init__(self, size):
        self.mapping = {}
        # Initialize the doubly linked list with one empty node.
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head
        self.listSize = 1
        # Adjust the size
        self.setSize(size)

    # can be used as len(a) where a is an object of class LRU
    def __len__(self):
        return len(self.mapping)

    # used as obj[key] to get value mapped to key
    def __getitem__(self, key):
        node = self.mapping[key]
        # Move this node as the most recently used
        self.changeNodeToMostRecentlyUsed(node)
        self.head = node
        return node.value

    # used as obj[key] = value to set the value mapped to key
    def __setitem__(self, key, value):
        # check if already in cache
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            # Move this node as the most recently used
            self.changeNodeToMostRecentlyUsed(node)
            self.head = node
            return
        # key-value not present in cache, now insert/replace in cache
        node = self.head.prev
        # if tail node is not empty, remove it as it is least recently used
        if not node.empty:
            del self.mapping[node.key]
        # Place the new key and value in the node
        node.empty = False
        node.key = key
        node.value = value
        self.mapping[key] = node
        # make this new node as the head as this is the most recently used
        self.head = node

    # Get an item - return default (None) if not present
    def get(self, key, default=None):
        if key not in self.mapping:
            return default
        return self[key]

    # put a key-value pair
    def put(self, key, value):
        self[key] = value

    # obj.clear() to clear all values in cache
    def clear(self):
        for node in self.iterList():
            node.empty = True
            node.key = None
            node.value = None
        self.mapping.clear()

    # increase or decrease size of the cache
    def setSize(self, size=None):
        if size is not None:
            assert size > 0
            if size > self.listSize:
                self.addTailNode(size - self.listSize)
            elif size < self.listSize:
                self.removeTailNode(self.listSize - size)
        return self.listSize

    def getSize(self):
        return self.listSize

    # Increases the size of the cache by inserting n empty nodes
    # at the tail of the list.
    def addTailNode(self, n):
        for i in range(n):
            node = Node()
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        self.listSize += n

    # Decreases the size of the list by removing n nodes from
    # the tail of the list.
    def removeTailNode(self, n):
        assert self.listSize > n
        for i in range(n):
            node = self.head.prev
            if not node.empty:
                del self.mapping[node.key]
            # remove node from list
            self.head.prev = node.prev
            node.prev.next = self.head
            node.prev = None
            node.next = None
            node.key = None
            node.value = None
        self.listSize -= n

    # change order of list, move node to head
    def changeNodeToMostRecentlyUsed(self, node):
        # remove node from list
        node.prev.next = node.next
        node.next.prev = node.prev
        # put it before head
        node.prev = self.head.prev
        node.next = self.head.prev.next
        # make node as new head
        node.next.prev = node
        node.prev.next = node

    # get an iterator that iterates over the non-empty nodes in the list
    def iterList(self):
        node = self.head
        for i in range(len(self.mapping)):
            yield node
            node = node.next
