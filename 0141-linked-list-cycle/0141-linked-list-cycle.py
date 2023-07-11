# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        seen = dict()

        while cur is not None:
            if cur in seen:
                return True

            seen[cur] = True
            cur = cur.next

        return False
        