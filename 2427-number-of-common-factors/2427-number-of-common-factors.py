class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_facts = self.find_factors(a)
        b_facts = self.find_factors(b)
        return len(a_facts & b_facts)
                

    def find_factors(self, n: int) -> set:
        facts = set()
        for i in range(1, n+1):
            if n % i == 0:
                facts.add(i)
        return facts        
            