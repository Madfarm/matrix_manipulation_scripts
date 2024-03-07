class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next and current_node.next.val != val:
                current_node = current_node.next
            if current_node.next:
                current_node.next = current_node.next.next

    def search(self, val):
        current_node = self.head
        while current_node:
            if current_node.val == val:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=' ')
            current_node = current_node.next
        print()


# Testing the LinkedList class
linked_list = LinkedList()

# Insertion
linked_list.insert(5)
linked_list.insert(10)
linked_list.insert(15)
linked_list.insert(20)

# Printing the list
linked_list.print_list()  # Output: 5 10 15 20

# Searching
print(linked_list.search(10))  # Output: True
print(linked_list.search(13))  # Output: False

# Deletion
linked_list.delete(15)
linked_list.print_list()  # Output: 5 10 20