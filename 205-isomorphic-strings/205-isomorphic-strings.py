class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        for i in range(len(s)):
            if not s[i] in smap.keys(): smap[s[i]] = i
            if not t[i] in tmap.keys(): tmap[t[i]] = i
            if not smap[s[i]] == tmap[t[i]]: return False
        return True
            