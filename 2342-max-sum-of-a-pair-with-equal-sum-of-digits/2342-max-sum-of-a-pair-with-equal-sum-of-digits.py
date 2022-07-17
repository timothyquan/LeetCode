class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        summap = {}
        for n in nums:            
            s = self.digit_sum(n)
            summap.setdefault(s, []) 
            summap[s].append(n)            
        
        pairsums = [sum(sorted(vals, reverse=True)[:2]) for vals in summap.values() if len(vals) > 1]
        return max(pairsums) if len(pairsums) > 0 else -1
            
    def digit_sum(self, num : int) -> int:
        s = 0
        while num > 0:
            s = s + (num % 10)
            num = num // 10
        return s