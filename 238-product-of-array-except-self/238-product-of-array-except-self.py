class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        exceptzeros = numprod = 1
        zerocount = 0
        for num in nums:
            numprod *= num
            if num:
                exceptzeros *= num
            else:
                zerocount += 1
        if zerocount > 1:
            return [0 for _ in range(len(nums))]
         
        
        allelse = []
        for num in nums:
            if num:
                allelse.append(numprod//num)
            else:
                prod = 1
                allelse.append(exceptzeros)
                    
                
        return allelse 
            
            
        
        