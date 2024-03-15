class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

def hash_function(key, size):
    return key % size

def insert(array, key, value):
    index = hash_function(key, len(array))
    array[index].insert(value)

def display(array):
    for i in range(len(array)):
        print("Bucket {}".format(i))
        array[i].print_list()

# Create an array of linked lists
array = [LinkedList() for _ in range(10)]

# Insert key-value pairs into the hash table
insert(array, 10, "Value1")
insert(array, 25, "Value2")
insert(array, 30, "Value3")

# Display the hash table
display(array)