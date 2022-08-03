# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            if root.val == subRoot.val:
                if self.is_sametree(root, subRoot):
                    return True
            return (self.isSubtree(root.left, subRoot) or 
                    self.isSubtree(root.right, subRoot))
            
    def is_sametree(self, r: TreeNode, s: TreeNode) -> bool:
        if not r and not s: return True
        elif not r or not s: return False
        if r.val == s.val:
            return (self.is_sametree(r.left, s.left) and
                    self.is_sametree(r.right, s.right))