from collections import namedtuple

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Creating nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

def lot(node, level=0):
    if node is None:
        return

    # Visit the node
    print(node.val)

    # Recursively visit siblings at the same level
    if node.left:
        lot(node.left, level)
    if node.right:
        lot(node.right, level)

    # Recursively visit children at the next level
    if node.left:
        lot(node.left.left, level + 1)
        lot(node.left.right, level + 1)
    if node.right:
        lot(node.right.left, level + 1)
        lot(node.right.right, level + 1)





lot(root)  # Output: 1, 2, 3