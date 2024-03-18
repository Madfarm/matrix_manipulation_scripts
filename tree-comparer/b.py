# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both trees are null
        if p is None and q is None:
            return True
        # One of p and q is null
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

# Test the function
# Create the first binary tree: 1, 2, 3
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# Create the second binary tree: 1, 2, 3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(5)

solution = Solution()
print(solution.isSameTree(root1, root2))  # Output: True

