class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        solcnt = [sum(s) for s in mat]
        weakcnt = set(sorted(solcnt)[:k])
        weakidx = []
        for wr in weakcnt:
            weakidx += [i for i,r in enumerate(solcnt) if r == wr]
        return weakidx[:k]