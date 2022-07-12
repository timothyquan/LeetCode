class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = newidx = 1 
        length = len(nums) - 1 
        if target == nums[0]: return 0
        elif target == nums[-1]: return length
        while newidx < length:
            newidx = idx * 2 if idx * 2 < length else length + 1
            res = self.find(nums[idx:newidx], target)
            if res != -1: return res + idx
            else: idx = newidx
        return -1    
                
                    
    def find(self, nums, target) -> int:        
        if target in nums:
            return nums.index(target)        
        else: return -1