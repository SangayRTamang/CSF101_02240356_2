class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    @staticmethod
    def merge_sorted(ll1, ll2):
        dummy = Node(0)
        tail = dummy
        p1, p2 = ll1.head, ll2.head

        while p1 and p2:
            if p1.data < p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        tail.next = p1 if p1 else p2
        merged_ll = LinkedList()
        merged_ll.head = dummy.next
        return merged_ll

# Test the find_middle method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("Middle element:", ll.find_middle()) 

# Test the detect_cycle method
print("Has cycle:", ll.detect_cycle()) 

# Creating a cycle for testing
ll.head.next.next.next.next = ll.head.next
print("Has cycle after adding cycle:", ll.detect_cycle())  

# Test remove_duplicates method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.remove_duplicates()
ll.display()

# Test merge_sorted method
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
merged_ll = LinkedList.merge_sorted(ll1, ll2)
merged_ll.display() 
