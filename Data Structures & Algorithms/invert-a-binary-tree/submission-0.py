# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        dummy=root
        dummy.left,dummy.right=dummy.right,dummy.left
        self.invertTree(dummy.left)
        self.invertTree(dummy.right)
        return root