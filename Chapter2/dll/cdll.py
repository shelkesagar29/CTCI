import unittest

# Implement circular doubly linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.sentinel = Node(data=None)
        self.len = 0

    def __len__(self):
        return self.len
    
    def __getitem__(self, index):
        if abs(index)>=self.len:
            raise IndexError("Index out of range")
        # take care of negative indexing like -1
        index = (self.len+index)%self.len
        current_index = 0
        current_node = self.sentinel.next
        while current_index!=index:
            current_node = current_node.next
            current_index+=1
        return current_node.data

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index<self.len:
            r = self.__getitem__(self.current_index)
            self.current_index+=1
            return r
        else:
            raise StopIteration
        
    def append(self, element):
        """
        Insert element before sentinel node.
        NOTE* Remember this is circular linked list
        """
        new_node = Node(data=element)
        # new_nodes previous node is node before sentinel node
        # if it exists
        if self.sentinel.prev:
            new_node.prev = self.sentinel.prev
        else:
            new_node.prev = self.sentinel

        # new_nodes next node is sentinel node itself
        new_node.next = self.sentinel

        # new_node will be the next node for the previous node of sentinel if 
        # it exists
        if self.sentinel.prev:
            # Corner case: First operation is append
            self.sentinel.prev.next = new_node

        # new node will be the previous node for the sentinel node
        self.sentinel.prev = new_node

        # Due to circular nature, if sentinel node has no next node,
        # new_node will be the next node
        if not self.sentinel.next:
            self.sentinel.next = new_node 
        self.len+=1

    def appendleft(self, element):
        """
        Insert element at the head i.e. after sentinel node
        """
        new_node = Node(data=element)
        # new_nodes next node will be the node after sentinel if it exists
        # else due to circular nature, it will be sentinel node
        if self.sentinel.next:
            new_node.next = self.sentinel.next
        else:
            new_node.next = self.sentinel
        # new_nodes prev node will be the sentinel node
        new_node.prev = self.sentinel

        # new node will be the previous node for the next node of the 
        # sentinel if it exists
        if self.sentinel.next:
            self.sentinel.next.prev = new_node
        # new node will be the next node of the sentinel node
        self.sentinel.next = new_node
        # Due to circular nature, if sentinel node has no next node,
        # new_node will be the next node
        if not self.sentinel.prev:
            self.sentinel.prev = new_node 
        self.len+=1

    def pop(self):
        """
        Delete and return element at the end of circular linked list.
        This is basically previous element of sentinel node.
        """
        if self.len<=0:
            print("Circular linked list is empty! Add elements first!")
            return
        r = self.sentinel.prev
        if r.prev == self.sentinel:
            # List has only one node except sentinel node
            # next element will be always sentinel node
            self.sentinel.next = None
            self.sentinel.prev = None
        else:
            # list has more than one nodes exceprt sentinel
            self.sentinel.prev = r.prev
            r.prev.next = self.sentinel
        self.len-=1
        return r.data

    def popleft(self):
        """
        Return and delete element after sentinel node.
        """
        if self.len<=0:
            print("Circular linked list is empty! Add elements first!")
            return
        r = self.sentinel.next
        if r.next == self.sentinel:
            # if next node is sentinal then list has only one node
            # previous node will be always sentinel
            self.sentinel.next = None
            self.sentinel.prev = None
        else:
            self.sentinel.next = r.next
            r.next.prev = self.sentinel
        self.len-=1
        return r.data

    def delete(self, index):
        """
        Delete node at given index
        """
        if not self.len:
            print("Circular linked list is empty! Add few elements first!")
            return

        if index>=self.len or index<0:
            raise IndexError("Index out of range")
        current_index = 0
        current_node = self.sentinel.next
        while current_index!=index:
            current_node = current_node.next
            current_index+=1
        
        # change links for prev and next node of the current node
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        self.len-=1
    

    def insert(self, index, element):
        """
        Insert element at given index
        """
        if index>self.len or index<0:
            raise IndexError("Index out of range")
        current_index = 0
        current_node = self.sentinel.next
        while current_index != (index-1):
            current_node = current_node.next
            current_index+=1

        # add node after current_node
        new_node = Node(data=element)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node 
        self.len+=1

    def print_cll(self):
        start_node = self.sentinel.next
        if start_node:
            while start_node.data is not None:
                print(start_node.data, end=" ")
                start_node = start_node.next
            print("")
        else:
            print("Circular linked list is empty! Add some elements first!")
            return

class TestCase(unittest.TestCase):
    def test_a_append(self):
        cll = CircularLinkedList()
        cll.appendleft(0)
        cll.append(1)
        cll.appendleft(2)
        cll.append(3)
        cll.appendleft(4)
        cll.append(5)
        cll.appendleft(6)
        cll.append(7)
        cll.appendleft(8)
        cll.append(9)
        self.assertEqual(cll[2], 4)
        self.assertEqual(cll[7], 5)
        self.assertEqual(len(cll), 10)
    
    def test_b_insert(self):
        cll = CircularLinkedList()
        cll.appendleft(0)
        cll.append(1)
        cll.appendleft(2)
        cll.append(3)
        cll.appendleft(4)
        cll.append(5)
        cll.appendleft(6)
        cll.append(7)
        cll.appendleft(8)
        cll.append(9)
        cll.insert(2, -30)
        self.assertEqual(cll[2], -30)
        self.assertEqual(len(cll), 11)

    def test_c_pop(self):
        cll = CircularLinkedList()
        cll.appendleft(0)
        cll.append(1)
        cll.appendleft(2)
        cll.append(3)
        cll.appendleft(4)
        cll.append(5)
        cll.appendleft(6)
        cll.append(7)
        cll.appendleft(8)
        cll.append(9)
        e_1 = cll.pop()
        self.assertEqual(e_1, 9)
        self.assertEqual(cll[-1],7)
        self.assertEqual(len(cll), 9)

    def test_d_popleft(self):
        cll = CircularLinkedList()
        cll.appendleft(0)
        cll.append(1)
        cll.appendleft(2)
        cll.append(3)
        cll.appendleft(4)
        cll.append(5)
        cll.appendleft(6)
        cll.append(7)
        cll.appendleft(8)
        cll.append(9)
        e_1 = cll.popleft()
        e_2 = cll.popleft()
        self.assertEqual(e_1, 8)
        self.assertEqual(e_2, 6)
        self.assertEqual(cll[0], 4)
        self.assertEqual(len(cll), 8)

    def test_e_delete(self):
        cll = CircularLinkedList()
        cll.appendleft(0)
        cll.append(1)
        cll.appendleft(2)
        cll.append(3)
        cll.appendleft(4)
        cll.append(5)
        cll.appendleft(6)
        cll.append(7)
        cll.appendleft(8)
        cll.append(9)
        cll.delete(0)
        self.assertEqual(cll[4], 1)

if __name__ == "__main__":
    unittest.main()
    



