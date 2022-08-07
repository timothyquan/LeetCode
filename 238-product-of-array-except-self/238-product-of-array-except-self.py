class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numprod = 1
        for num in nums:
            numprod *= num
         
        
        allelse = []
        for i,num in enumerate(nums):
            if not num == 0:
                allelse.append(numprod//num)
            else:
                prod = 1
                for i2, num2 in enumerate(nums):
                    if not i == i2:
                        prod *= num2
                allelse.append(prod)
                    
                
        return allelse 
            
            
        
        