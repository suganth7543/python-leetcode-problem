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
        dummy = ListNode()   # sentinel
        tail = dummy

        p, q = list1, list2
        while p and q:
            if p.val <= q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        # attach remaining nodes (one of p or q is None)
        tail.next = p if p else q
        return dummy.next