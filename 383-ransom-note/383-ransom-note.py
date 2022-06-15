class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for l in r:
            if not (r[l] <= m[l]): 
                return False
        return True
