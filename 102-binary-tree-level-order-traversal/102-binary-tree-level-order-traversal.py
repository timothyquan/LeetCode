# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodemap = {}
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root: self.records(root)
        return self.nodemap.values()
    
        
    def records(self, node, level = 0):
        level += 1
        self.nodemap.setdefault(level, [])
        self.nodemap[level].append(node.val)
        for child in [node.left, node.right]:
            if child: self.records(child, level)
                
    
        
    