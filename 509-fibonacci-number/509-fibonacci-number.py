class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for _ in range(0,n):
            b += a
            a = b-a
        return a
            
        
             