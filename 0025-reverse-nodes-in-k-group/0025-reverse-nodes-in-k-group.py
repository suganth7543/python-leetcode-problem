# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        head2=None
        head1=tail=head
        prev_tail=None
        
        def rev(start,end):
            cur=start
            prev=None

            while cur!=end:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            start.next=end
            
            return prev

        
        while True:
            tmp=tail
            for i in range(k):
                if tmp:
                    tmp=tmp.next
                else:
                    return head2 if head2 else head
            
            tail=tmp
            new_head=rev(head1,tail)

            if head2 is None:
                head2=new_head
            
            if prev_tail:
                prev_tail.next=new_head

            prev_tail=head1
            head1=tail
        return head2
            
                