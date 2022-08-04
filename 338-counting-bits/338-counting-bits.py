class Solution:
    def countBits(self, n: int) -> List[int]:
        bins = [bin(i)[2:] for i in range(n+1)]
        res = []
        for b in bins:
            res.append(0)
            for c in b:
                if c == '1':
                    res[-1] += 1
        return res

