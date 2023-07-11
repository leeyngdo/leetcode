# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(None); cur = None

        while True:
            if list1 is None and list2 is None:
                return head.next
            elif list1 is None:
                if head.next is None:
                    head.next = list2
                else:
                    cur.next = list2
                return head.next
            elif list2 is None:
                if head.next is None:
                    head.next = list1
                else:
                    cur.next = list1
                return head.next
            else:
                if list1.val <= list2.val:
                    if head.next is None: # initial
                        head.next = list1
                        cur = list1
                    else:
                        cur.next = list1
                        cur = cur.next
                    list1 = list1.next
                else:
                    if head.next is None: # initial
                        head.next = list2
                        cur = list2
                    else:
                        cur.next = list2
                        cur = cur.next
                    list2 = list2.next
    
        return head.next