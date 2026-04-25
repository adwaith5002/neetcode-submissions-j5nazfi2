# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        sum=0
        head=ListNode()
        curr=l1
        i=1
        while(curr):
            n1+=curr.val*i
            i*=10
            curr=curr.next
        
        curr=l2
        i=1
        while(curr):
            n2+=curr.val*i
            i*=10
            curr=curr.next
        sum=n1+n2

        print(sum)
        res=head
        if sum==0:
            return head

        while(sum!=0):
            val=sum%10
            print(val)
            res.next=ListNode(val)
            sum=sum//10
            res=res.next
        
        return head.next
        