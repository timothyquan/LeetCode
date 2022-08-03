class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += add
                add = 0 
                break
        if add:
            digits.insert(0,add)
        return digits                
            
            
        
        
            