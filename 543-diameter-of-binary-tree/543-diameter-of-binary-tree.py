# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxlength = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        else:
            self.dfs(root)
        return self.maxlength
           
    def dfs(self, node):
        if not node:
            return 0            
        rlen = self.dfs(node.right)
        llen = self.dfs(node.left)
        self.maxlength = rlen + llen if rlen + llen > self.maxlength else self.maxlength
        return max(rlen, llen) + 1