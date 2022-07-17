class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        out = [] 
        for q in queries:
            etrimmed = enumerate([int(str(n)[-(q[1]):]) for n in nums])
            kth = sorted(etrimmed, key=itemgetter(1))[q[0]-1][0]
            out.append(kth)             
        return out 
    