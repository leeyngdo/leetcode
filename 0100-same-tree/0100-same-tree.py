from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            if not p and not q: return True
            return False
        if p.val != q.val: return False

        p_queue = deque(); q_queue = deque()
        p_queue.append(p); q_queue.append(q)
        while p_queue and q_queue:
            node_p = p_queue.popleft(); node_q = q_queue.popleft()
            if not node_p and node_q: return False
            if node_p and not node_q: return False
            if not node_p and not node_q: continue

            if node_p.val != node_q.val: return False
            p_queue.append(node_p.left); q_queue.append(node_q.left)
            p_queue.append(node_p.right); q_queue.append(node_q.right)

        if p_queue != q_queue: return False
        else: return True
        

