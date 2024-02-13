from typing import Optional

def bfs(node, level=0, queue=None):
    if node is None:
        return

    # Initialize the queue if not provided
    if queue is None:
        queue = []

    # Enqueue the node
    queue.append(node)

    # Recursively visit the node's children
    if node.left:
        bfs(node.left, level+1, queue)
    if node.right:
        bfs(node.right, level+1, queue)

    # If the node has no children, dequeue and visit it
    if not node.left and not node.right:
        queue.pop(0)
        print(node.val)

    # Recursively visit the next node in the queue
    if queue:
        bfs(queue[0], level, queue)



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

print(bfs(root))  # Output: 1, 2, 3