# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
        
        
    def invert(self, node):
        if node:
            swap = node.right
            node.right = node.left
            node.left = swap
                   
            for node in [node.left, node.right]:
                self.invert(node)
