import unittest

class Node:
    def __init__(self, animal=None):
        self.animal = animal
        self.next = None
        self.prev = None

class AnimalShelter:
    def __init__(self):
        self.sentinel_head = Node()
        self.sentinel_tail = Node()
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head
    
    def values(self):
        r = []
        current = self.sentinel_head.next
        while current.animal != None:
            r.append(current.animal)
            current = current.next
        return r

    # O(1) operation
    def enqueue(self, animal):
        # Append operation in doubly linked list
        new_node = Node(animal=animal)
        latest_node = self.sentinel_tail.prev
        if latest_node == self.sentinel_head:
            # Shelter is empty
            new_node.next = self.sentinel_tail
            new_node.prev = self.sentinel_head
            self.sentinel_tail.prev = new_node
            self.sentinel_head.next = new_node
        else:
            # shelter has animals already
            new_node.next = self.sentinel_tail
            new_node.prev = latest_node
            latest_node.next = new_node
            self.sentinel_tail.prev = new_node
            
    def dequque_any(self):
        # Remove first element
        oldest_node = self.sentinel_head.next
        if oldest_node == self.sentinel_tail:
            # There are no animals in the shelter
            return None
        else:
            # There are animals in the shelter so return oldest animal
            r = oldest_node.animal
            self.sentinel_head.next = oldest_node.next
            oldest_node.next.prev = self.sentinel_head
            return r

    def dequque_cat(self):
        # Remove first oldest cat
        oldest_node = self.sentinel_head.next
        if oldest_node == self.sentinel_tail:
            return None
        else:
            # Travel till oldest node is not cat or we go till the end of the list
            while oldest_node.animal != "cat" and oldest_node.animal != None:
                oldest_node = oldest_node.next
            if oldest_node == self.sentinel_tail:
                return None
            else:
                r = oldest_node.animal
                self.sentinel_head.next = oldest_node.next
                oldest_node.next.prev = self.sentinel_head
                return r

    def dequque_dog(self):
        # Remove first oldest dog
        oldest_node = self.sentinel_head.next
        if oldest_node == self.sentinel_tail:
            return None
        else:
            # Travel till oldest node is not cat or we go till the end of the list
            while oldest_node.animal != "dog" and oldest_node.animal != None:
                oldest_node = oldest_node.next
            if oldest_node == self.sentinel_tail:
                return None
            else:
                r = oldest_node.animal
                self.sentinel_head.next = oldest_node.next
                oldest_node.next.prev = self.sentinel_head
                return r

class TestCases(unittest.TestCase):
    def test_empty(self):
        a = AnimalShelter()
        self.assertEqual(a.dequque_any(), None)
        self.assertEqual(a.dequque_cat(), None)
        self.assertEqual(a.dequque_dog(), None)
    
    def test_enqueue(self):
        a = AnimalShelter()
        a.enqueue("cat")
        a.enqueue("dog")
        a.enqueue("cat")
        a.enqueue("dog")
        self.assertEqual(a.values(), ["cat","dog","cat","dog"])

    def test_dequeue_any(self):
        a = AnimalShelter()
        a.enqueue("cat")
        a.enqueue("dog")
        a.enqueue("cat")
        a.enqueue("dog")
        a.enqueue("dog")
        a.enqueue("dog")
        self.assertEqual(a.dequque_any(), "cat")
        self.assertEqual(a.dequque_any(), "dog")
        self.assertEqual(a.dequque_any(), "cat")
        self.assertEqual(a.dequque_any(), "dog")
        self.assertEqual(a.dequque_any(), "dog")
        self.assertEqual(a.dequque_any(), "dog")
        self.assertEqual(a.dequque_any(), None)

    def test_dequeue_cat(self):
        a = AnimalShelter()
        a.enqueue("dog")
        a.enqueue("dog")
        self.assertEqual(a.dequque_cat(), None)
        a.enqueue("cat")
        self.assertEqual(a.dequque_cat(), "cat")
        self.assertEqual(a.dequque_cat(), None)

    def test_dequeue_dog(self):
        a = AnimalShelter()
        a.enqueue("cat")
        a.enqueue("cat")
        self.assertEqual(a.dequque_dog(), None)
        a.enqueue("dog")
        self.assertEqual(a.dequque_dog(), "dog")
        self.assertEqual(a.dequque_dog(), None)

if __name__ == "__main__":
    unittest.main()