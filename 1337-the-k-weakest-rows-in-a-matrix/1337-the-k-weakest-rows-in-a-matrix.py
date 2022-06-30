#version 2: the first one I used numpy, which was 2 lines but ended up being in the bottom 5% for efficiency. 
#here I attempt to use a list as a hash table to see if it is any faster. 
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        solmap = [ [] for m in range(len(mat[0])+1)]
        for idx,val in enumerate(mat):
            solmap[sum(val)].append(idx)
        weakest = []
        i = 0
        
        print(solmap)
        while len(weakest) < k:
            weakest += solmap[i]
            i+=1
        return weakest[:k]    