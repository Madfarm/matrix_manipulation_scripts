class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def delete(self, val):
        if self.head:
            if self.head.val == val:
                self.head = self.head.next
            else:
                current = self.head
                while current.next and current.next.val != val:
                    current = current.next
                if current.next:
                    current.next = current.next.next

    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()


# Example usage
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.print_list()  # Output: 5 10 15

ll.delete(10)
ll.print_list()  # Output: 5 15

print(ll.search(15))  # Output: True
print(ll.search(20))  # Output: False