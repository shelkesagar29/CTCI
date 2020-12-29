import unittest
from linkedlist import LinkedList

def solution1(ll):
    """
    Time Complexity: O(n) where n is the length of the linked list
    Space Complexity: O(n/2)= O(n)
    Args:
        ll (LinkedList): linked list object
    Returns:
        True: If palindrome
        False: If not a palindrome.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!

    # setp 1, traverse linked list to fill stack with first half
    slow = ll.head.next
    fast = ll.head.next
    stack = []
    while fast.data!=None and fast.next.data!=None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast.data:
        slow = slow.next

    while stack:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True

def solution2(ll):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Another approach to check for palindrome is matching orginal and reversed string.
    """
    raise NotImplementedError
    
class TestClass(unittest.TestCase):
    test_cases = [
        ([1,2,3,4,3,2,1],True),
        ([1],True),
        ([1,2,2,1],True),
        ([1,2,3,4,1],False),
        ([],True)
    ]

    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                input_ll = LinkedList(initial_members=t_input)
                self.assertEqual(test_function(input_ll), e_output)

if __name__ == "__main__":
    unittest.main()
