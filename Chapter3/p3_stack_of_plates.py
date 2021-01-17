import unittest

class Node:
    def __init__(self, data=None):
        self.data=data
        # pointer to the next node in current stack
        self.next_e = None
        # pointer to the next stack in the set of stacks
        self.next_s = None
        # Number of elements under this head
        self.n_elements = 0

class SetOfStacks:
    def __init__(self, s_size):
        """
        Set of stacks implemented here can be visualized as follows
        N = number of stacks
        M = Elements in each stack
        sos ---> Stack1head ----> Stack2head ----> Stack3head .......... StackNhead
                    |                |                                      |
                    |                |                                      |
                    e1s1            e1s2                                   e1sN
                    e2s1            e2s2                                   e2sN
                    e3s1            e3s2                                   e3sN
                    .                .                                      .
                    .                .                                      .
                    eMs1            eMs2                                   eMsN
        Elements are pushed in order from Stack1 to StackN. 
        StackN is selected only when stackN-1 is full. 
        """
        self.stack_size = s_size
        # sentinel head for set of stacks
        self.sos = Node(data=None)
        self.stack_heads = [Node(data=None)]
        self.sos.next_s = self.stack_heads[0]
        self.current_stack_head = self.stack_heads[0]
        self.stacks_in_set = 1
    
    def values(self):
        r = []
        for h in self.stack_heads:
            current_stack = []
            current = h.next_e
            if current:
                while current!=None:
                    current_stack.append(current.data)
                    current = current.next_e
                r.append(current_stack)
        return r

    def _change_head_if_possible(self):
        current_head_index = 0
        for i in range(self.stacks_in_set):
            if self.stack_heads[i]==self.current_stack_head:
                current_head_index=i
        
        # if current head index is not zero, head can be shifted left
        if current_head_index!=0:
            self.current_stack_head = self.stack_heads[current_head_index-1]
            # detach empty stack
            self.current_stack_head.next_s = None
            _ = self.stack_heads.pop()
            self.stacks_in_set-=1

    def _create_new_stack(self):
        new_stack_head = Node(data=None)
        self.stack_heads[-1].next_s = new_stack_head
        self.stack_heads.append(new_stack_head)
        self.current_stack_head = new_stack_head
        self.stacks_in_set+=1

    # O(1)
    def push(self, data):
        if self.current_stack_head.n_elements==self.stack_size:
            self._create_new_stack()
        new_node = Node(data=data)
        top_node = self.current_stack_head.next_e
        if top_node:
            # stack is not empty
            self.current_stack_head.next_e = new_node
            new_node.next_e = top_node
            self.current_stack_head.n_elements+=1
        else:
            # stack is empty
            self.current_stack_head.next_e = new_node
            self.current_stack_head.n_elements+=1

    def _pop_invisible(self):
        top_node = self.current_stack_head.next_e
        if top_node:
            # current stack has elements
            r = top_node.data
            self.current_stack_head.next_e = top_node.next_e
            return r
        else:
            # current stack is empty
            return None

    # O(1)
    def pop(self):
        top_node = self.current_stack_head.next_e
        if top_node:
            # current stack has elements
            r = top_node.data
            self.current_stack_head.next_e = top_node.next_e
            return r
        else:
            # current stack is empty
            # current head should move to previous head if there are any previously
            # filled stacks
            self._change_head_if_possible()
            pir = self._pop_invisible()
            return pir

    # O(1)
    def popatindex(self, index):
        """
        Args:
            index (int): stack index starting from 1
        """
        if index>self.stacks_in_set:
            raise Exception("Not enough stacks in the set")
        # Actual index where stack heads are stored starts from zero
        index-=1
        top_node = self.stack_heads[index].next_e
        if top_node:
            # current stack has elements
            r = top_node.data
            self.current_stack_head.next_e = top_node.next_e
            return r
        else:
            # current stack is empty
            return None
        
class TestCases(unittest.TestCase):
    def test_empty(self):
        sos = SetOfStacks(3)
        self.assertEqual(sos.values(), [])
        self.assertEqual(sos.pop(), None)
        self.assertEqual(sos.popatindex(1), None)
        with self.assertRaises(Exception) as context:
            sos.popatindex(4)
        self.assertTrue("Not enough stacks in the set" in str(context.exception))

    def test_one_stack(self):
        sos = SetOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        self.assertEqual(sos.values(), [[3,2,1]])
        _ = sos.pop()
        self.assertEqual(sos.pop(), 2)
    
    def test_many_stacks(self):
        sos = SetOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        # new stack should start from here
        sos.push(10)
        sos.push(20)
        sos.push(30)
        # new stack should start from here
        sos.push(100)
        sos.push(200)
        self.assertEqual(sos.values(), [[3,2,1],[30,20,10],[200,100]])
        self.assertEqual(sos.pop(), 200)
    
    def test_pop_at_index(self):
        sos = SetOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        # new stack should start from here
        sos.push(10)
        sos.push(20)
        sos.push(30)
        # new stack should start from here
        sos.push(100)
        sos.push(200)
        self.assertEqual(sos.popatindex(2), 30)

    def test_pop(self):
        sos = SetOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        # new stack should start from here
        sos.push(10)
        self.assertEqual(sos.pop(), 10)
        self.assertEqual(sos.pop(), 3)
        self.assertEqual(sos.pop(), 2)
        self.assertEqual(sos.pop(), 1)
        self.assertEqual(sos.pop(), None)
        

if __name__ == "__main__":
    unittest.main()






