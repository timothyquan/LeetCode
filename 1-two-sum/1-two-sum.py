class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            seek = target - n
            if seek in nums[i+1:]:
                return [i, nums[i+1:].index(seek) + i + 1]
      
                
       