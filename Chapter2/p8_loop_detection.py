import unittest
from DS.linkedlist import LinkedList

def solution1(ll):
    """
    Time Complexity: O(n) where n is the length of the linked list
    Space Complexity: O(1)
    Args:
        ll (LinkedList): linked list object
    Returns:
        data: Node value where loop starts if LL has loop.
        -1: If LL has no loop.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!

    # setp 1, Detect whether linked list has loop or not
    slow = ll.head.next
    fast = ll.head.next
    has_loop = False
    is_first = True
    while fast.data != None and fast.next.data !=None:
        if slow.data == fast.data:
            if is_first:
                is_first = False
                pass
            else:
                has_loop = True
                break
        slow = slow.next
        fast = fast.next.next
    # setp2, detect the starting of the loop
    # here we take slow pointer to the head, fast remains at same position
    # increment both pointers by one and where they meet is the loop start
    # over simplified proof: https://stackoverflow.com/a/33149978
    if not has_loop:
        return -1
    slow = ll.head.next
    while True:
        if slow.data == fast.data:
            return slow.data
        slow = slow.next
        fast = fast.next

    """
    Bonus: Remove the loop.
    keep the slow pointer steady after loop start is detected.
    Increment fast pointer by one until slow pointer is the next.
    Set tail node as the next node of the node immediately before slow pointer.

    while fast.next.data!=slow.data:
        fast = fast.next
    
    fast.next = ll.tail
    """

def solution2(ll):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    In this solution, we use set.
    """
    h_set = set()
    current_node = ll.head.next
    while current_node.data != None:
        if current_node.data in h_set:
            # if loop needs to be removed, set tail node as the next of the previous node.
            return current_node.data
        else:
            h_set.add(current_node.data)
        current_node = current_node.next
    return -1
    
    
class TestClass(unittest.TestCase):
    test_ll_1 = LinkedList(initial_members=[1,2])
    dup_node = test_ll_1.append(value=3)
    _ = test_ll_1.append(value=4)
    last_node = test_ll_1.append(5)
    last_node.next = dup_node

    test_ll_2 = LinkedList(initial_members=[1,2,3,4,5,6,7,8])

    test_cases = [
        (test_ll_1, 3),
        (test_ll_2, -1)
    ]
    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
