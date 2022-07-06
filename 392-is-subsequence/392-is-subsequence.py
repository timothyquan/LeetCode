class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        for c in s:              
            if not c in it: return False
        return True