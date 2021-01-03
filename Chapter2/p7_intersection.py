import unittest
from DS.linkedlist import LinkedList

def solution1(ll_1, ll_2):
    """
    Time Complexity: O(n) where n is the length of the linked list
    Space Complexity: O(1)
    Args:
        ll_1 (LinkedList): first linked list object
        ll_2 (LinkedList): second linked list object
    Returns:
        data: Node value where linked lists intersect.
        False: If linked lists does not intersect.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!

    if ll_1.tail != ll_2.tail:
        return False

    longer = ll_1 if len(ll_1)>len(ll_2) else ll_2
    shorter = ll_1 if len(ll_1)<len(ll_2) else ll_2

    diff = len(longer)-len(shorter)
    longer_current = longer.head.next
    # go ahead by diff in longer linked list
    while diff:
        longer_current = longer_current.next
        diff-=1

    shorter_current = shorter.head.next

    # go till tail sentinel node. At this point both ll have same length
    while shorter_current is not longer_current:
        shorter_current = shorter_current.next
        longer_current = longer_current.next
    return longer_current.data
    
    
class TestClass(unittest.TestCase):
    shared_ll = LinkedList(initial_members=[10,20,30])
    a = LinkedList(initial_members=[1,2,3,4,5,6])
    b = LinkedList(initial_members=[-1,-2,-3])

    a_current = a.head.next
    while a_current.next.data!=None:
        a_current = a_current.next
    a_current.next = shared_ll.head.next
    a.tail = shared_ll.tail

    b_current = b.head.next
    while b_current.next.data!=None:
        b_current = b_current.next
    b_current.next = shared_ll.head.next
    b.tail = shared_ll.tail

    test_cases = [
        (a, b, 10)
    ]
    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input_1, t_input_2, e_output in self.test_cases:
                self.assertEqual(test_function(t_input_1, t_input_2), e_output)

if __name__ == "__main__":
    unittest.main()
