class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        out = [] 
        for q in queries:
            etrimmed = [(int(str(n)[-(q[1]):]), i) for i,n in enumerate(nums)]
            kth = sorted(etrimmed)[q[0]-1][1]
            out.append(kth)             
        return out 
    