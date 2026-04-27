# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grp_prev=dummy
        while(True):
            i=0
            count=grp_prev
            while(count and i<k):
                    i+=1
                    count=count.next
            kth=count
            if not kth:
                break
            groupnnext=kth.next

            reverse=grp_prev.next
            prev=kth.next
            while(reverse!=groupnnext):
                temp=reverse.next
                reverse.next=prev
                prev=reverse
                reverse=temp
            temp=grp_prev.next
            grp_prev.next=kth            
            grp_prev=temp
        return dummy.next