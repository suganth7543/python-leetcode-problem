# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next==None:
            return head
        first = head 
        second = first.next 
        third = second.next
        swappedTail = self.swapPairs(third)
        second.next = first
        first.next = swappedTail
        return second
        

        