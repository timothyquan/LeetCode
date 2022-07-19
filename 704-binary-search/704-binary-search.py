class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1        
        
        while right >= left:            
            pivot = (right + left)//2
            if nums[pivot] == target: return pivot
            elif nums[pivot] > target: right = pivot - 1
            elif nums[pivot] < target: left = pivot + 1

        
                
        return -1 