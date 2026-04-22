# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=list1
        b=list2
        curr_a=a
        curr_b=b
        dummy=res=ListNode()
        while(curr_a and curr_b):
            aleft=curr_a.val
            bleft=curr_b.val
            if aleft<bleft:
                res.next=curr_a
                curr_a=curr_a.next
            else:
                res.next=curr_b
                curr_b=curr_b.next
            res=res.next
        res.next=curr_a or curr_b
        return dummy.next

