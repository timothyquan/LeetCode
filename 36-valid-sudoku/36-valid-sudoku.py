class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = [['.'] * 9 for _ in range(9)] 
        boards = [[] for _ in range(9)] 
        board_idx = {(0,0): 0, (0,1): 1, (0,2): 2,
                     (1,0): 3, (1,1): 4, (1,2): 5,
                     (2,0): 6, (2,1): 7, (2,2): 8}
        
        for ri,r in enumerate(board):
            if self.contains_duplicate(r): return False             
            for ci,c in enumerate(r):
                boards[board_idx[(ri//3,ci//3)]].append(c)
                cols[ci][ri] = c
                
        for c in cols:
            if self.contains_duplicate(c): return False
            
        for b in boards:
            if self.contains_duplicate(b): return False
            
        return True
        
                
                 
        
    def contains_duplicate(self, l: List[str])-> bool:
        lm = {}
        for c in l:
            if not c == '.':
                lm[c] = lm.get(c, -1) + 1
        return any(lm.values())