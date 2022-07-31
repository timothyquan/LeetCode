class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nums = [num for num in nums if num > 0]
        while any(nums):
            m = min(nums)    
            nums = [num - m for num in nums if num - m > 0]
            count += 1
            
        return count    
                

            
        