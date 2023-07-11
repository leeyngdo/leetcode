# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            l_h, l_bal = self.helper(root.left)
            r_h, r_bal = self.helper(root.right)

            return abs(l_h - r_h) <= 1 and (l_bal and r_bal)

    def helper(self, root):
        """
        Return: height of tree, whether it is balanced
        """
        if root is None:
            return 0, True
        else:
            l_h, l_bal = self.helper(root.left)
            r_h, r_bal = self.helper(root.right)
            bal = abs(l_h - r_h) <= 1 and (l_bal and r_bal)
            return max(l_h, r_h) + 1, bal