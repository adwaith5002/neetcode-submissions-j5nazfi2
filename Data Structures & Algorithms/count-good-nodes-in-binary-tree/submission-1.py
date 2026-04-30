# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maximum=-math.inf
        return self.dfs(root,maximum)

    def dfs(self,root,maximum):
        if not root:
            return 0
        count=0
        if root.val>=maximum:
            maximum=root.val
            count=1
        count+=self.dfs(root.left,maximum)
        count+=self.dfs(root.right,maximum)
        return count
