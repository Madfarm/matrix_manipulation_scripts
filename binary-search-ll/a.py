class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

def binary_search(ll, target):
    if ll is None:
        return "Linked list is empty"

    low = ll.head
    high = None

    while low:
        fast = low
        slow = low

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if slow.data == target:
            return True
        elif slow.data < target:
            low = slow.next
        else:
            if high is None:
                high = slow
            low = slow.next

        if high is not None and low.data > high.data:
            return False

    return False

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print(binary_search(ll, 3))  # Output: True
print(binary_search(ll, 6))  # Output: False