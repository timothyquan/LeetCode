class Solution:
    def fib(self, n: int) -> int:
        def rec_fib(n, l=[0,1], i=0):
            if i < n: 
                return rec_fib(n, [l[1], l[0]+l[1]], i+1)
            return l[0] 
        
                   
        return rec_fib(n)
             