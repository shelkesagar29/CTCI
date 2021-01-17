import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.sentinel = Node(data=None)
        self.len = 0

    def values(self):
        r = []
        current = self.sentinel.next
        if current:
            while current != None:
                r.append(current.data)
                current = current.next
        return r

    def push(self, data):
        # push node to the stack
        new_node = Node(data=data)
        top_node = self.sentinel.next
        if top_node:
            # Stack is not empty
            self.sentinel.next = new_node
            new_node.next = top_node
        else:
            # Stack is empty
            self.sentinel.next = new_node
        self.len+=1
    
    def pop(self):
        # Remove and return top element from the stack
        top_node = self.sentinel.next
        if top_node:
            # There is top node, return it and fix linking
            self.len-=1
            self.sentinel.next = top_node.next
            return top_node.data
        else:
            return None
    
    def peek(self):
        # Return top element from the stack
        top_node = self.sentinel.next
        if top_node:
            return top_node.data
        else:
            return None
    
    def is_empty(self):
        # Return True if stack is empty
        top_node = self.sentinel.next
        if top_node:
            return False
        else:
            return True

class TestCases(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        self.assertEqual(s.is_empty(), True)
        self.assertEqual(s.peek(), None)
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.peek(), 30)
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        self.assertEqual(s.pop(), None)

if __name__ == "__main__":
    unittest.main()