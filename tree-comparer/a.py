# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

# Create two binary trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Create an instance of the Solution class
solution = Solution()

# Call the isSameTree method
print(solution.isSameTree(tree1, tree2))  # Output: True