class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        add = 1
        for i,digit in enumerate(digits):
            if digit == 9:
                digits[i] = 0
            else:
                digits[i] += add
                add = 0 
                break
        if add:
            digits.append(add)
        return digits[::-1]
                
            
            
        
        
            