class Solution:
    def greatestLetter(self, s: str) -> str:
        lset = set(s)
        uplows = [""]
        for l in lset:
            if l.isupper() and l.lower() in lset:
                uplows.append(l)
        return sorted(uplows)[-1]        
           
               