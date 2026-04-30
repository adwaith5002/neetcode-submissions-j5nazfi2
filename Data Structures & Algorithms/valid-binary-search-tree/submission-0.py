# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lower= -math.inf
        upper=math.inf
        return self.check(root,float("-inf"), float("inf"))
    
    def check(self, root: Optional[TreeNode], lower, upper) -> bool:    
        if not root:
            return True
        if root.val< upper and root.val>lower:
            left=self.check(root.left, lower, min(upper, root.val))
            right= self.check(root.right,max(lower, root.val), upper)
            return left and right
        else:
            return False