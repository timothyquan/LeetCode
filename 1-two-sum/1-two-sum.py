class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            seek = target - n
            found = [i2 + i + 1 for i2,v in enumerate(nums[i+1:]) if v == seek]
            if found:
                return [i, found[0]]
      
                
       