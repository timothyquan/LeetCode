class Solution:
    def longestPalindrome(self, s: str) -> int:
        charmap = {}
        for c in s: 
            charmap.setdefault(c, 0)
            charmap[c] += 1
            
        length = sum([(c//2) * 2 for c in charmap.values()])
        return length if length == len(s) else length + 1
                
            
        