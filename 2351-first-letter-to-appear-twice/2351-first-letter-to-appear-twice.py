class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cmap = {}
        for c in s:
            cmap.setdefault(c, 0)
            cmap[c] += 1
            if cmap[c] > 1: 
                return c
            
            
       