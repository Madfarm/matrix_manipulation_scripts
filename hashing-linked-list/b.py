class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, value):
        return hash(value) % self.size

    def insert(self, value):
        index = self.hash_function(value)
        if self.table[index] is None:
            self.table[index] = Node(value)
        else:
            node = self.table[index]
            while node.next:
                node = node.next
            node.next = Node(value)

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                node = self.table[i]
                while node:
                    print(f"Index {i}: {node.value}", end=", ")
                    node = node.next
                print()

# Testing the function
hash_table = HashTable(10)
hash_table.insert("apple")
hash_table.insert("banana")
hash_table.insert("cherry")
hash_table.insert("date")
hash_table.insert("elderberry")
hash_table.display()