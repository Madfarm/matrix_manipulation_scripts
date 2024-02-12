from collections import namedtuple

Node = namedtuple('Node', ['val', 'left', 'right'])

tree = Node(1, Node(2, None, None), Node(3, None, None))

def bfs(root):
    if root is None:
        return

    # Visit the node
    print(root.val)

    # Recursively visit left child
    bfs(root.left)

    # Recursively visit right child
    bfs(root.right)





bfs(tree)  # Output: 1, 2, 3