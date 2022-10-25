class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortnums = sorted(nums)
        f, l = 0, len(nums) - 1
        while f < l:
            twosum = sortnums[f] + sortnums[l]
            if twosum == target:
                return self.indexof(nums, sortnums[f], sortnums[l]) 
            elif twosum > target:
                l -= 1
            elif twosum < target:
                f += 1
                
    def indexof(self, nums: List[int], t1: int, t2: int):
        if t1 != t2:
            return [nums.index(t1), nums.index(t2)]
        else:
            i1 = nums.index(t1)            
            i2 = nums[i1+1:].index(t1) + i1 + 1
            return [i1,i2]
            