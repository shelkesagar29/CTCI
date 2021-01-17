import unittest

class TioStack:
    def __init__(self, num_stacks, stack_size=4):
        # Size of each stack
        self.stack_size = stack_size
        # Stack as initially fixed size list
        self.stack = [0]*num_stacks*stack_size
        # Current capacities of each stack.
        # When stack is full, capacity is increased 
        self.stack_capacities = [stack_size]*num_stacks
        # Current size of each stack
        self.stack_sizes = [0]*num_stacks
        # Current tops of each stack
        self.stack_tops = [i*stack_size for i in range(num_stacks)]
        # Number of stacks
        self.n_stacks = num_stacks
    
    def pp(self):
        print("Stack:{}".format(self.stack))
        print("Stack Capacities:{}".format(self.stack_capacities))
        print("Stack Size:{}".format(self.stack_sizes))
        print("Stack Tops:{}".format(self.stack_tops))
    
    def values(self):
        return self.stack
        
    def extend_and_shift(self, start_index, stack):
        """
        When particular stack fills up, stack size is increased by 'stack_size' and 
        all the elements are shifted to the right.
        """
        cp_from_index = len(self.stack)-1
        self.stack.extend([0]*self.stack_size)
        cp_to_index = len(self.stack)-1
        if stack == self.n_stacks-1:
            # For last stack, we don't have to shift elements
            pass
        else:
            while cp_from_index != start_index-1:
                self.stack[cp_to_index] = self.stack[cp_from_index]
                cp_to_index-=1
                cp_from_index-=1
            
        # update stack tops. Only stacks after current stack will be 
        # affected
        for i in range(stack+1, len(self.stack_tops)):
            self.stack_tops[i]+=self.stack_size
            
        # Update stack capacity
        self.stack_capacities[stack]+=self.stack_size
        

    # O(1) Amortized
    def push(self, data, stack):
        if stack>self.n_stacks:
            raise Exception("Stack number exceeds number of stacks")
        # indexing starts from zero!
        stack-=1
        current_stack_size = self.stack_sizes[stack]
        current_stack_capacity = self.stack_capacities[stack]
        current_stack_top = self.stack_tops[stack]
        if current_stack_size == current_stack_capacity:
            # Particular stack has no space
            # increase size by 'stack_size' and move all the elements to the right
            self.extend_and_shift(self.stack_capacities[stack], stack)
            self.stack[current_stack_top] = data
            self.stack_sizes[stack]+=1
            self.stack_tops[stack]+=1
        else:
            # Particular stack has space left
            self.stack[current_stack_top] = data
            self.stack_sizes[stack]+=1
            self.stack_tops[stack]+=1

    # O(1)
    def pop(self, stack):
        if stack>self.n_stacks:
            raise Exception("Stack number exceeds number of stacks")
        # indexing starts from zero
        stack-=1
        if self.stack_sizes[stack]==0:
            # stack is empty
            return None
        r = self.stack[self.stack_tops[stack]-1]
        self.stack_tops[stack]-=1
        self.stack_sizes[stack]-=1
        return r

    # O(1)
    def peek(self, stack):
        if stack>self.n_stacks:
            raise Exception("Stack number exceeds number of stacks")
        # indexing starts from zero
        stack-=1
        if self.stack_sizes[stack]==0:
             # stack is empty
            return None
        return self.stack[self.stack_tops[stack]-1]

class TioStack2:
    def __init__(self, num_stacks):
        self.stack = [[] for i in range(num_stacks)]
        self.n_stacks = num_stacks
    
    # O(1) Amortized
    def push(self, data, stack):
        """
        Args:
            data(int): Data to add to the stack
            stack (int): Stack number starting from 1. 1.... num_stacks
        Returns:
            None
        """
        if stack>self.n_stacks:
            raise Exception("Stack number exceeds number of stacks")
        self.stack[stack].append(data)

    # O(1) Amortized
    def pop(self, stack):
        if stack>self.n_stacks:
            raise Exception("Stack number exceeds number of stacks")
        try:
            r = self.stack[stack].pop()
            return r
        except IndexError:
            # Intended for when stack is empty
            return None

class TestCases(unittest.TestCase):
    def test_one(self):
        a = TioStack(3)
        self.assertEqual(a.pop(1), None)
        self.assertEqual(a.peek(1), None)
        with self.assertRaises(Exception) as context:
            a.peek(4)
        self.assertTrue("Stack number exceeds number of stacks" in str(context.exception))
    
    def test_two(self):
        a = TioStack(3)
        a.push(1,1)
        a.push(2,1)
        a.push(10,2)
        a.push(100,3)
        self.assertEqual(a.values(), [1,2,0,0,10,0,0,0,100,0,0,0])
    
    def test_three(self):
        a = TioStack(3)
        a.push(1,1)
        a.push(2,1)
        a.push(10,2)
        a.push(100,3)
        a.push(3,1)
        a.push(4,1)
        a.push(20,2)
        a.push(200,3)
        a.push(5,1)
        self.assertEqual(a.values(), [1,2,3,4,5,20,0,0,10,20,0,0,100,200,0,0])

    def test_four(self):
        a = TioStack(3)
        a.push(1,1)
        self.assertEqual(a.pop(1), 1)
        a.push(2,1)
        a.push(3,1)
        a.push(10,2)
        a.push(100,3)
        self.assertEqual(a.values(), [2,3,0,0,10,0,0,0,100,0,0,0])

if __name__ == "__main__":
    unittest.main()
