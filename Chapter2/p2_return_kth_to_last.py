import unittest
from DS.linkedlist import LinkedList

def solution1(ll, k):
    """
    Time Complexity: O(n) where n is length of linked list
    Space Complexity: O(1)
    Here we first get length (l) of the linked list [we start count from 1].
    kth element to the last is (l-k)th element from first.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!
    
    # step 1: get length of the linked list.
    current_node = ll.head.next
    if current_node is ll.tail:
        return -1
    ll_length = 0
    while current_node.data != None:
        ll_length+=1
        current_node = current_node.next
    if k>=ll_length:
        return -1
    
    # step 2: get distance to the kth element
    distance_to_kth = ll_length - k
    running_distance = 1
    current_node = ll.head.next
    while running_distance!=distance_to_kth:
        current_node = current_node.next
        running_distance+=1
    return current_node.data

def solution2(ll, k):
    """
    In this solution, we use the concept of two pointers.
    backward pointer lags forward pointer by k.
    Thus when forward pointer reaches the end, backward pointer is at position k.
    Time Complexity: O(n) where n is the length of the linked list.
    Space Complexity: O(1)
    """
    if ll.head.next is ll.tail:
        return -1
    fp_index = 0
    bp_index = 0 - k
    fp = ll.head.next
    bp = ll.head.next
    while fp.data != None:
        fp = fp.next
        if bp_index>=0:
            bp = bp.next
        fp_index+=1
        bp_index+=1
    return bp.data
    
class TestClass(unittest.TestCase):
    test_cases = [
        # (linked_list, k, target)
        ([1,2,3,4,5,6],1,5),
        ([],6,-1),
        ([100,200,300],2,100),
        ([235],0,235)
    ]

    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, k, e_output in self.test_cases:
                input_ll = LinkedList(initial_members=t_input)
                p_out = solution1(input_ll, k)
                self.assertEqual(p_out, e_output)

if __name__ == "__main__":
    unittest.main()
