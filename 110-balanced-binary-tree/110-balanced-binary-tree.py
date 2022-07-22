# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
        
    def dfs(self, node) -> list:
        if not node:
            return [True, 0]
    
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        bal = abs(left[1]-right[1]) <= 1 and left[0] and right[0]
            
        return [bal, 1 + max(left[1], right[1])]
      