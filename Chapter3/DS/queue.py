# This is doubly ended queue implementation
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.sentinel_head = Node(data=None)
        self.sentinel_tail = Node(data=None)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head
        self.len = 0

    def values(self):
        r = []
        current = self.sentinel_head.next
        while current.data!=None:
            r.append(current.data)
            current = current.next
        return r

    def append(self, data):
        # append element at the end
        new_node = Node(data=data)
        self.len+=1
        last_node = self.sentinel_tail.prev
        if last_node == self.sentinel_head:
            # Queue is empty
            new_node.next = self.sentinel_tail
            new_node.prev = self.sentinel_head
            self.sentinel_head.next = new_node
            self.sentinel_tail.prev = new_node
        else:
            # Queue has elements
            new_node.next = self.sentinel_tail
            new_node.prev = last_node
            last_node.next = new_node
            self.sentinel_tail.prev = new_node

    def appendleft(self, data):
        new_node = Node(data=data)
        self.len+=1
        first_node = self.sentinel_head.next
        if first_node == self.sentinel_tail:
            # Queue is empty
            new_node.next = self.sentinel_tail
            new_node.prev = self.sentinel_head
            self.sentinel_head.next = new_node
            self.sentinel_tail.prev = new_node
        else:
            # Queue has elements
            new_node.prev = self.sentinel_head
            new_node.next = first_node
            first_node.prev = new_node
            self.sentinel_head.next = new_node
    
    def pop(self):
        # Remove and return last node
        last_node = self.sentinel_tail.prev
        r = None
        if last_node == self.sentinel_head:
            # Queue is empty
            return r
        else:
            # Queue has elements
            self.len-=1
            r = last_node.data
            last_node.prev.next = self.sentinel_tail
            self.sentinel_tail.prev = last_node.prev
            return r

    def popleft(self):
        # Remove and return first node
        first_node = self.sentinel_head.next
        r = None
        if first_node == self.sentinel_tail:
            # Queue is empty
            return r
        else:
            # Queue has elements
            self.len-=1
            r = first_node.data
            first_node.next.prev = self.sentinel_head
            self.sentinel_head.next = first_node.next
            return r

    def is_empty(self):
        first_node = self.sentinel_head.next
        if first_node == self.sentinel_tail:
            return True
        else:
            return False

class TestCases(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        self.assertEqual(q.values(), [])
        self.assertEqual(q.pop(), None)
        self.assertEqual(q.popleft(), None)
        self.assertEqual(q.is_empty(), True)
        q.append(10)
        self.assertEqual(q.pop(), 10)
        q.append(10)
        q.append(20)
        self.assertEqual(q.popleft(), 10)
        self.assertEqual(q.pop(), 20)
        q.append(30)
        q.append(40)
        self.assertEqual(q.values(), [30, 40])
        self.assertEqual(q.is_empty(), False)
        q.appendleft(-10)
        self.assertEqual(q.values(), [-10, 30, 40])

if __name__ == "__main__":
    unittest.main()
