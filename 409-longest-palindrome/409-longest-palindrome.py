class Solution:
    def longestPalindrome(self, s: str) -> int:
        charmap = {}
        for c in s: 
            charmap.setdefault(c, 0)
            charmap[c] += 1
        dromlen = 0
        odds = False
        for c in (charmap.values()):
            if c % 2 != 0:
                odds = True
                c -= 1
            dromlen += c
        return dromlen + odds
                
            
        