from DS.stack import Stack
import unittest

class QueueViaStacks:
    # FIFO queue
    def __init__(self):
        self.p_stack = Stack()
        self.s_stack = Stack()

    def add(self, item):
        self.p_stack.push(item)

    def _move_to_secondary(self):
        p_current = self.p_stack.pop()
        while p_current!= None:
            self.s_stack.push(p_current)
            p_current = self.p_stack.pop()

    def _move_to_primary(self):
        s_current = self.s_stack.pop()
        while s_current!= None:
            self.p_stack.push(s_current)
            s_current = self.s_stack.pop()

    def remove(self):
        # get oldest element which is at the bottom of the stack.
        # Move elements from primary to secondary stack
        self._move_to_secondary()
        # get return value
        r = self.s_stack.pop()
        # move elements back to primary stack
        self._move_to_primary()
        return r

    def peek(self):
        self._move_to_secondary()
        r = self.s_stack.peek()
        self._move_to_primary()
        return r

    def is_empty(self):
        return self.p_stack.is_empty()

class TestCases(unittest.TestCase):
    def test_qvs_empty(self):
        qvs = QueueViaStacks()
        self.assertEqual(qvs.peek(), None)
        self.assertEqual(qvs.remove(), None)
        self.assertEqual(qvs.is_empty(), True)

    def test_qvs(self):
        qvs = QueueViaStacks()
        qvs.add(10)
        qvs.add(20)
        qvs.add(30)
        qvs.add(40)
        self.assertEqual(qvs.peek(), 10)
        self.assertEqual(qvs.remove(), 10)
        self.assertEqual(qvs.peek(), 20)
        self.assertEqual(qvs.is_empty(), False)

if __name__ == "__main__":
    unittest.main()
