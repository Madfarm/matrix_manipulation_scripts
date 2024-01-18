class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    
    def __repr__(self):
        return f"Node({self.value})"

def generate_binary_tree(depth):
    nodes = [Node(i) for i in range(2**(depth-1))]

    print(len(nodes))

    children = [[nodes[2*i] if 2*i < len(nodes) else None, nodes[2*i+1] if 2*i+1 < len(nodes) else None] for i in range(len(nodes))]

    tree = [Node(nodes[i], children=children[i]) for i in range(len(nodes))]

    return tree

tree = generate_binary_tree(3)
print(tree)