class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        moffsets = len(grid) - 2 #run through the first 3x3 and then however many offsets
        noffsets = len(grid[0]) - 2
        maxhoursum = 0
        for mo in range(moffsets):
            for no in range(noffsets):
                curhoursum = 0
                for m in range(3):
                    if m == 1:
                        curhoursum += grid[m+mo][1+no]
                    else:       
                        for n in range(3):
                            curhoursum += grid[m+mo][n+no]
                if curhoursum > maxhoursum:
                    maxhoursum = curhoursum 
                print(curhoursum)   
        return maxhoursum
                        
    

        