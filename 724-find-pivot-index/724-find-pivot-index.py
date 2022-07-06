class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        front = 0
        back = sum(nums[1:]) 
        if not back: return 0
        for idx in range(1, len(nums)):
            back -= nums[idx]
            front += nums[idx-1]
            if front == back:
                return idx           
        return -1    
            
        