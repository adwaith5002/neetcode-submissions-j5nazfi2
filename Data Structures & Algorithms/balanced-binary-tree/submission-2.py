# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        isBalanced=True
        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            res=abs(left-right)
            if res>1:
                isBalanced=False
            return max(left,right)
        dfs(root)
        return isBalanced
