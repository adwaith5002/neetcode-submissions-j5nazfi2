# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2) :
        head=ListNode()
        res=head
        while(l1!=None and l2!=None):
                if l1.val<l2.val:
                    res.next=l1
                    l1=l1.next
                else:
                    res.next=l2
                    l2=l2.next
                res=res.next
        if l1:
            res.next=l1
        elif l2:
            res.next=l2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while(len(lists)>1):
            mergedList=[]
            for i in range(0,len(lists),2):
                l2=lists[i+1] if i+1<len(lists) else None
                mergedList.append(self.mergeTwoLists(lists[i],l2))
            lists=mergedList
        return lists[0]