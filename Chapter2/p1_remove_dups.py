import unittest
from DS.linkedlist import LinkedList

def solution1(ll):
    """
    Time Complexity: O(n) where n is length of linked list
    Space Complexity: O(n)
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!
    h_set = set()
    current_node = ll.head
    # travel till node before sentinel tail node
    while current_node.next.data != None:
        if current_node.next.data in h_set:
            # next node is already in h_set thus is duplicate
            current_node.next = current_node.next.next
            ll.len-=1
        else:
            # add data to h_set
            h_set.add(current_node.next.data)
            current_node=current_node.next
    return ll
    
class TestClass(unittest.TestCase):
    test_cases = [
        ([1,2,3,4,4,2,1],[1,2,3,4]),
        ([1,1,1,1,1,1],[1]),
        ([],[]),
        ([235],[235]),
        ([1,2,3,4,4],[1,2,3,4])
    ]

    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                input_ll = LinkedList(initial_members=t_input)
                processed_ll = solution1(input_ll)
                self.assertEqual(processed_ll.values(), e_output)

if __name__ == "__main__":
    unittest.main()
