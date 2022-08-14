class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edgemap = {}
        for i,edge in enumerate(edges):
            edgemap[edge] = edgemap.get(edge, 0) + i
        return sorted(edgemap.items(), key=lambda kv: (kv[1], -kv[0]))[-1][0]


            
            
        