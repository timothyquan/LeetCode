class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = set(nums)
        full = {num for num in range(len(nums)+1)}
        return full.difference(miss).pop()
        
      