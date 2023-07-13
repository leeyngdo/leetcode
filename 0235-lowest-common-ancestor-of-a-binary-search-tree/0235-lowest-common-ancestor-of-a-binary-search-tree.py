from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if node.val <= max(p.val, q.val) and node.val >= min(p.val, q.val):
                return node
            else:
                if node.val > max(p.val, q.val):
                    return dfs(node.left)
                else:
                    return dfs(node.right)
        
        return dfs(root)
