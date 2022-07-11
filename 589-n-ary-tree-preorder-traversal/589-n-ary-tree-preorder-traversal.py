"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    
    
    def __init__(self):
        self.vals = []
    
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            self.rec_child(root)
        return self.vals

    def rec_child(self, node):
        self.vals.append(node.val)
        for child in node.children:
            self.rec_child(child)
    