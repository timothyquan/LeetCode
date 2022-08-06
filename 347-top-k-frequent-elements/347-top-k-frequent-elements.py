class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num]  = freqmap.get(num, 0) + 1
            
        heap = [(-count, val) for val,count in freqmap.items()] 
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)] 
        