class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        front,back = 0, sum(nums)
        for idx,num in enumerate(nums):
            back -= num
            if front == back:
                return idx           
            front += num 
            
        return -1    
            
        