# This module is used in all test cases.
# This linked list implmentation uses sentinel head and tail nodes.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return "Data:{}, Prev:{}, Next:{}".format(self.data, self.prev, self.next)

class LinkedList:
    def __init__(self, initial_members=None):
        # keep head and tail sentinel node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.len = 0
        if initial_members is not None:
            # Initial members are always appended.
            self.appendmultiple(values=initial_members)
    
    def __str__(self):
        # printable represntation of the linked list
        r = self.values()
        return "->".join([str(e) for e in r])
    
    def __len__(self):
        return self.len

    def values(self):
        # return linked list elements as python list
        r=[]
        if not self.len:
            return r
        current_node = self.head.next
        while current_node.data != None:
            r.append(current_node.data)
            current_node = current_node.next
        return r

    def append(self, value):
        # append node before tail
        new_node = Node(data=value)
        new_node.next = self.tail
        current_node = self.head.next
        if current_node is self.tail:
            self.head.next = new_node
        else:
            # travel till node just before the tail
            while current_node.next.data != None:
                current_node = current_node.next
            # new_node will be the next node for curret_node
            current_node.next = new_node
        self.len+=1
        # giving access to the newly added nodes is important for few questions
        return new_node

    def appendleft(self, value):
        # append node after head
        new_node = Node(data=value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.len+=1
        # giving access to the newly added nodes is important for few questions
        return new_node

    def appendmultiple(self, values):
        # append multiple values before tail. Input is python list
        if not values:
            # empty list
            return
        for v in values:
            self.append(v)

    def appendleftmultiple(self, values):
        # append multiple values before head
        if not values:
            return
        for v in values:
            self.appendleft(v)

class DoubleLinkedList(LinkedList):
    def __init__(self, initial_members=None):
        super().__init__(initial_members=initial_members)
        self.tail.prev = self.head

    def append(self, value):
        # append node before tail node in the doubly linked list
        new_node = Node(data=value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.len+=1

    def appendleft(self, value):
        # append node after head
        new_node = Node(data=value)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.len+=1

if __name__ == "__main__":
    print("This module implements single and double linked lists \
    primarily used for testing all codes in this chapter.")
    
