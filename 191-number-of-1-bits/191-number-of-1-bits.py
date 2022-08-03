class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in bin(n) if i == '1'])