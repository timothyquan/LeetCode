class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            s1,s2 = heapq.heappop(stones), heapq.heappop(stones)
            if not (s1 == s2):
                heapq.heappush(stones, s1 - s2)
                
            
        return 0 if len(stones) == 0 else stones[0] * -1
        