class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def contains_dups(l : dict):
            
            pass
                    
                    
        cols = [{} for _ in range(9)]
        subs = [{} for _ in range(9)]
        
        for ri, r in enumerate(board):
            subrow = ri // 3
            row = {}
            for ci, c in enumerate(r):                
                subcol = ci // 3
                subidx = (subrow * 3) + subcol
                if c != '.':
                    row[c] = row.get(c, -1) + 1
                    cols[ci][c] = cols[ci].get(c, -1) + 1
                    subs[subidx][c] = subs[subidx].get(c, -1) + 1
                if ci == 8 and any(row.values()):
                    return False
                if ri == 8 and any(cols[ci].values()):
                    print(cols[ci])
                    return False
                if ri % 3 == 2 and ci % 3 == 2 and any(subs[subidx].values()):                    
                    return False
        [print(r) for r in board]
        return True        
                    
                    
                    