import unittest
from LRU import LRU
import random

class TestLRU(unittest.TestCase):

    # checks if the len of cache becomes 0 after clearing cache
    def testClear(self):
        obj = LRU(2)
        obj.put(1,2)
        obj.put(3,4)
        self.assertEqual(len(obj), 2)
        obj.clear()
        self.assertEqual(len(obj), 0)


    # checks if updating value of key gets the correct value
    def testGetPut(self):
        obj = LRU(1)
        obj.put(1,2)
        self.assertEqual(obj.get(1), 2)
        obj.put(1,4)
        # checkk if value is updated
        self.assertEqual(obj.get(1), 4)
        # check if default value is returned if key isn't there
        self.assertEqual(obj.get(2, "not found"), "not found")


   
    # checks if setsize resizes the list
    def testSetSize(self):
        obj = LRU(2)
        self.assertEqual(obj.listSize, 2)
        obj.setSize(4)
        head = obj.head.next
        count = 1
        while head != obj.head:
            count += 1
            head = head.next
        self.assertEqual(count, 4)


    # test if least recently used item is actually removed
    def testLRUItemIsActuallyRemoved(self):
        obj = LRU(4)
        obj.put(1,1)
        obj.put(2,1)
        obj.put(3,1)
        obj.put(4,1)
        obj.put(1,1) # 2 becomes lru
        obj.put(5,1)
        # now get(2) should return none
        self.assertEqual(obj.get(2), None)


    # check if head is actually after node
    def testChangeNodeToMostRecentlyUsed(self):
        obj = LRU(3)
        obj.put(1,1)
        obj.put(2,1)
        obj.put(3,1)
        node = obj.mapping[1] # points to 1
        obj.changeNodeToMostRecentlyUsed(node)
        self.assertEqual(obj.head, node.next)


    def testAddTailNode(self):
        obj = LRU(1)
        obj.addTailNode(1) # add 1 node
        self.assertEqual(obj.listSize, 2)
        r = random.randrange(10)
        obj.addTailNode(r) # add r nodes
        self.assertEqual(obj.listSize, r+2)


if __name__ == '__main__':
    unittest.main()