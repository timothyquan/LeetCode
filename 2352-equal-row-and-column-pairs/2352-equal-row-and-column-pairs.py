class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        cols = [[] for row in grid]
        
        for row in grid:
            for i,n in enumerate(row):
                cols[i].append(n)
                
        count = 0
        for col in cols:
            for row in grid:
                if col == row:
                    count += 1
        return count            
                
            

        