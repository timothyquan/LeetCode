class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edgemap = {}
        edgeheap = []
        heapq.heapify(edgeheap)
        for i,edge in enumerate(edges):
            edgemap[edge] = edgemap.get(edge, 0) + i
            heapq.heappush(edgeheap, (-edgemap[edge], edge))
        #return sorted(edgemap.items(), key=lambda kv: (kv[1], -kv[0]))[-1][0]
        
                
        return heapq.heappop(edgeheap)[1]

            
            
        