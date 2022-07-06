class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        for i in range(len(s)):            
            if not smap.setdefault(s[i], i) == tmap.setdefault(t[i], i):
                return False
        return True
            