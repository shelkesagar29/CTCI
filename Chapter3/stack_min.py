import unittest

class Node:
    def __init__(self, data, sub_min):
        self.data = data
        self.substack_min = sub_min
        self.next = None


class Stack:
    def __init__(self):
        self.sentinel = Node(data=None, sub_min=None)

    def values(self):
        # Return dictionary with key value pair. Key is stack element and value is substack min
        r = {}
        top_node = self.sentinel.next
        while top_node:
            r[top_node.data] = top_node.substack_min
            top_node = top_node.next
        return r

    def push(self, data):
        # add to normal stack
        top_node = self.sentinel.next
        if top_node:
            substack_min = min(data, top_node.substack_min) 
            new_node = Node(data=data, sub_min=substack_min)
            if data < self.last_min:
                self.last_min = data
            # stack is not empty
            new_node.next = top_node
            self.sentinel.next = new_node
        else:
            # stack is empty
            new_node = Node(data=data, sub_min=data)
            self.last_min = data
            self.sentinel.next = new_node

    def pop(self):
        top_node = self.sentinel.next
        if top_node:
            # stack is not empty
            self.sentinel.next = top_node.next
            return top_node.data
        else:
            # stack is empty
            return None

    def min(self):
        top_node = self.sentinel.next
        if top_node:
            return top_node.substack_min
        else:
            return None

class TestCases(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        s.push(3)
        s.push(10)
        s.push(2)
        s.push(15)
        self.assertEqual(list(s.values().keys()), [15,2,10,3])
        self.assertEqual(s.pop(), 15)
        s.push(8)
        self.assertEqual(s.min(), 2)
        s.push(1)
        self.assertEqual(s.min(), 1)
        _ = s.pop()
        self.assertEqual(s.min(), 2)

if __name__ == "__main__":
    unittest.main()
