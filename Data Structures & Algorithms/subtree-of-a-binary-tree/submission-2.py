# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubTree=False
        if not subRoot:
            return True
        if not root:
            return isSubTree
        if (root.val==subRoot.val):
            equal=self.isSame(root,subRoot)
            left=self.isSubtree(root.left, subRoot)
            right=self.isSubtree(root.right,subRoot)
            isSubTree=equal or left or right
        else:
            left=self.isSubtree(root.left,subRoot)
            right=self.isSubtree(root.right,subRoot)
            isSubTree=left or right
        return isSubTree
    def isSame(self,root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val==subRoot.val:
            left=self.isSame(root.left,subRoot.left)
            right=self.isSame(root.right,subRoot.right)
            return left and right
        else:
            return False