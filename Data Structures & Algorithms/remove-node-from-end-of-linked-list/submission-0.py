# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len=0
        slow=head
        while(slow):
            len+=1
            slow=slow.next
        
        i=0
        prev=None
        curr=head
        if len-n==0:
            return head.next

        while(curr):
            if (i==len-n):
                temp=curr.next
                curr.next=None
                curr=prev
                curr.next=temp
            prev=curr
            curr=curr.next
            i+=1
        return head
        