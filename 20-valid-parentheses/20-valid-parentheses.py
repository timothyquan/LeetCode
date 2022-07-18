class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')':'(', 
               '}':'{',
               ']':'['}
        sl = []
        for c in s:
            if c in pmap:
                if sl and sl[-1] == pmap[c]:
                    sl.pop()
                else:
                    return False
            else:
                sl.append(c)
                
        return not sl
            
       

                    
                
                
            