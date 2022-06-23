import numpy as np

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        scl = np.array([sum(l) for l in mat])      
        return (scl.argsort(kind='mergesort')[:k])