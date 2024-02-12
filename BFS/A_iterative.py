from collections import deque, namedtuple

def bfs(root):
    # Create a queue to store the nodes to visit
    queue = deque([root])

    while queue:
        # Dequeue the front node
        node = queue.popleft()

        # Visit the node
        print(node.val)

        # Add the left and right children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

Node = namedtuple('Node', ['val', 'left', 'right'])

tree = Node(1, Node(2, None, None), Node(3, None, None))

bfs(tree)  # Output: 1, 2, 3