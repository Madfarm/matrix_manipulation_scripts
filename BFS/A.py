from typing import Optional

def bfs(root):
    if root is None:
        return

    # Visit the node
    print(root.val)

    # Recursively visit left child
    bfs(root.left)

    # Recursively visit right child
    bfs(root.right)

class Node:
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.val = val
        self.left = left
        self.right = right

tree = Node(1, Node(2), Node(3))

print(bfs(tree))  # Output: 1, 2, 3