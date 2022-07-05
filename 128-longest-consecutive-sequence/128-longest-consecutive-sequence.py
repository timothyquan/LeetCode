class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur = []
        mlen = 0
        for i in sorted(set(nums)):
            if len(cur) == 0: cur = [i]
            elif (cur[-1]) == i-1: cur.append(i)
            else: 
                cur = [i]
            if len(cur) > mlen: mlen = len(cur)
        return mlen   
