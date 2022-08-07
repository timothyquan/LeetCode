class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap = {}
        for string in strs:
            anagrammap.setdefault(tuple(sorted(string)), []).append(string)
            
        print(anagrammap)
        return anagrammap.values()
           
            