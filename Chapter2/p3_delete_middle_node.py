import unittest
from DS.linkedlist import LinkedList

def solution1(node):
    """
    Time Complexity: O(n) where n is length of linked list
    Space Complexity: O(1)
    NOTE* middle node means any node except left most or right most
    e.g.
    a->b->c->d->e->f
    except a and f, all nodes are considered middle node.

    If we are told to delete c, we are given access to the only node c.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!
    node.data = node.next.data
    node.next = node.next.next
    
class TestClass(unittest.TestCase):
    def test_template(self):
        input_ll = LinkedList(initial_members=[10,20,30,40])
        node_to_be_deleted = input_ll.append(value=0)
        input_ll.appendmultiple(values=[50,60,70])
        solution1(node_to_be_deleted)
        self.assertEqual(input_ll.values(), [10,20,30,40,50,60,70])

if __name__ == "__main__":
    unittest.main()
