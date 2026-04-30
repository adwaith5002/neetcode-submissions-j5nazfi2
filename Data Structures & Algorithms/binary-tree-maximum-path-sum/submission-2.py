# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-math.inf

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            curr=0
            left=dfs(root.left)
            right=dfs(root.right)
            curr=left+right+root.val
            res=max(res, curr)
            curr=max(root.val,max(left,right)+root.val)
            res=max(res, curr)
            return curr

        dfs(root)
        return res