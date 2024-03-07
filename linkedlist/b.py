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

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

# Create a linked list and add some nodes to it
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Print the linked list
print("Original linked list:")
linked_list.print_list()

# Reverse the linked list
linked_list.reverse()

# Print the reversed linked list
print("Reversed linked list:")
linked_list.print_list()