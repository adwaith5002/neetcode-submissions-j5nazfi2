# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        future_tail=ListNode()
        curr_head=head
        curr=head
        step=0
        while(curr):
            i=0
            curr_head=curr
            count=curr
            while(count):
                    i+=1
                    count=count.next
            if i<k:
                future_tail.next=curr_head
                return head
            else:
                step+=1
                j=1
                reverse=curr
                prev=None
                while(j<=k):
                    temp=reverse.next
                    reverse.next=prev
                    prev=reverse
                    reverse=temp
                    j+=1
                
                curr_tail=prev
                future_tail.next=curr_tail
                if step==1:
                    head=curr_tail
                future_tail=curr_head
                curr=temp
        
        return head