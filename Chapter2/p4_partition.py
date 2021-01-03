import unittest
from DS.linkedlist import LinkedList

def solution1(ll, pivot):
    """
    Time Complexity: O(n) where n is the length of the linked list
    Space Complexity: O(n)
    Args:
        ll (LinkedList): linked list object
        pivot (int): Pivot for partition
    Returns:
        ll (LinkedList): linked list object with partitioned numbers.
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!

    before_list = LinkedList()
    before_list_current = before_list.head
    after_list = LinkedList()

    current_node = ll.head.next
    while current_node.data != None:
        if current_node.data < pivot:
            before_list.append(current_node.data)
            before_list_current = before_list_current.next
        else:
            after_list.append(current_node.data)
        current_node = current_node.next

    before_list_current.next = after_list.head.next
    return before_list
    
class TestClass(unittest.TestCase):
    test_cases = [
        ([3,5,8,5,10,2,1], [3,2,1,5,8,5,10])
    ]

    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                input_ll = LinkedList(initial_members=t_input)
                processed_ll = test_function(input_ll, 5)
                self.assertEqual(processed_ll.values(), e_output)

if __name__ == "__main__":
    unittest.main()
