from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        heap = []
        
        # Step 1: Push the head of each list into heap
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        # Dummy head for the result linked list
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: Pop smallest and push next node from that list
        while heap:
            val, i, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next