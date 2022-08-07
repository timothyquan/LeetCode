class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num]  = freqmap.get(num, 0) + 1
            
        #heap = [(-count, val) for val,count in freqmap.items()] 
        #heapq.heapify(heap)
        #return [heapq.heappop(heap)[1] for i in range(k)] 
        
        #sortdict = sorted(freqmap.items(), key=itemgetter(1))
        #return [i[0] for i in sortdict[-k:]] 
        
        heap = []
        heapq.heapify(heap)
        for num,freq in freqmap.items():
            heapq.heappush(heap, (-freq, num))
        
        return [heapq.heappop(heap)[1] for i in range(k)]