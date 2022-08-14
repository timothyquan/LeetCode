class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edgemap = {}
        for i,edge in enumerate(edges):
            edgemap[edge] = edgemap.get(edge, 0) + i
        #return sorted(edgemap.items(), key=lambda kv: (kv[1], -kv[0]))[-1][0]
        
        highkey, highval = 0, 0
        for kv in edgemap.items():
            if kv[1] > highval:
                highkey, highval = kv
            elif kv[1] == highval and highkey > kv[0]:
                highkey, highval = kv 
                
        return highkey

            
            
        