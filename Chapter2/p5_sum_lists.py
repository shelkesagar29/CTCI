import unittest
from linkedlist import LinkedList

def solution1(number1_ll, number2_ll, sum_ll):
    """
    Digits are stored in the reverse order (Reverse order is easy and intuitive).
    Args:
        numbers1_ll (LinkedList): number 1 in the form of linked list
        numbers2_ll (LinkedList): number 2 in the form of linked list
    Returns:
        sum_ll (LinkedList): Sum of number 1 and number 2 in the form of linked list

    e.g.
      7->1->6
    + 5->9->2
    ---------
      2->1->9

      617+295 = 912
    
      3->9->3
    + 5->3
    ---------
      8->2->4

      393+035 = 428 
    NOTE* Singly linked list is used.
    Time Complexity: O(m+n) where m,n is the length of the input linked lists.
    Space Complexity: O(m+n) output linked list 
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!
    number1_ll_current = number1_ll.head.next
    number2_ll_current = number2_ll.head.next
    carry = 0
    while number1_ll_current.data != None and number2_ll_current.data!=None:
        carry_added_sum = (number1_ll_current.data + number2_ll_current.data)+carry
        t_sum = carry_added_sum%10
        carry = carry_added_sum//10
        sum_ll.append(value=t_sum)
        number1_ll_current = number1_ll_current.next
        number2_ll_current = number2_ll_current.next
    
    # add carry to remaining digits of the longer number
    if number1_ll_current.data:
        while number1_ll_current.data!=None:
            carry_added_sum = number1_ll_current.data+carry
            t_sum = carry_added_sum%10
            carry = carry_added_sum//10
            sum_ll.append(value=t_sum)
            number1_ll_current = number1_ll_current.next

    if number2_ll_current.data:
        while number2_ll_current.data!=None:
            carry_added_sum = number2_ll_current.data+carry
            t_sum = carry_added_sum%10
            carry = carry_added_sum//10
            sum_ll.append(value=t_sum)
            number2_ll_current = number2_ll_current.next

    # add carry node if there is
    if carry:
        sum_ll.append(value=carry)

def solution2_helper(number1_ll_head, number2_ll_head, sum_ll):
    """
    Digits are stored in the forward order.
    Recursive way can take us to the end of the linked list and start adding from
    there.
    Args:
        numbers1_ll_head (Node): Head of the linked list representing number 1
        numbers2_ll (Node): Head of the linked list representing number 2
        carry (int): Initial carry which is 0.
    Returns:
        sum_ll (LinkedList): Sum of number 1 and number 2 in the form of linked list.

    e.g.
      6->1->7
    + 2->9->5
    ---------
      9->1->2

      617+295 = 912
    
      3->9->3
    +    3->5
    ---------
      4->2->8

      393+035 = 428 
    NOTE* Singly linked list is used.
    Time Complexity: O(n) where n is the length of the longer linked list
    Space Complexity: O(n) 
    """
    # Note that ll implementation uses sentinel head and tail node
    # In the solution, no other information than linked list head is used!
    raise NotImplementedError

def solution2(ll1_head, ll2_head, sum_ll, carry):
    solution2_helper(ll1_head, ll2_head, sum_ll)

class TestClass(unittest.TestCase):
    test_cases_reverse = [
        ([5,9,3,7,1,6],[9,8,5,7,1,4],[4,8,9,4,3,0,1]),
        #([2,3,6,7],[1,5,9],[3,8,5,8]),
        #([3,9,3],[5,3],[8,2,4]),
        #([2,1],[8],[0,2])
    ]
    
    def test_reverse(self):
        for test_case in self.test_cases_reverse:
            number1_ll = LinkedList(initial_members=test_case[0])
            number2_ll = LinkedList(initial_members=test_case[1])
            sum_ll = LinkedList()
            solution1(number1_ll, number2_ll, sum_ll)
            self.assertEqual(sum_ll.values(), test_case[2])

    def test_forward(self):
        for test_case in self.test_cases_reverse:
            number1_ll = LinkedList(initial_members=reversed(test_case[0]))
            number2_ll = LinkedList(initial_members=reversed(test_case[1]))
            sum_ll = LinkedList()
            solution2(number1_ll.head, number2_ll.head, sum_ll, 0)
            self.assertEqual(sum_ll.values(), test_case[2])

if __name__ == "__main__":
    unittest.main()
