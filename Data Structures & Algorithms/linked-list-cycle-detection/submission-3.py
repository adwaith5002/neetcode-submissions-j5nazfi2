# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        fast=head
        while(fast.next!=None):
            fast=fast.next.next
            head=head.next
            if fast==None:
                break
            if fast==head:
                return True
        return False