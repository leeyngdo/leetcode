from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        output = [[root.val]]; 
        queue = deque(); queue.append((root, 0))
        while queue:
            node, lv = queue.popleft()
            if node.left:
                queue.append((node.left, lv + 1))
                if lv + 1 > len(output) - 1: output.append([])
                output[lv + 1].append(node.left.val)
            if node.right:
                queue.append((node.right, lv + 1))
                if lv + 1 > len(output) - 1: output.append([])
                output[lv + 1].append(node.right.val)

        return output
