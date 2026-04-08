from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                item = board[r][c]

                if item == ".":
                    continue
                elif (item in row[r] or
                    item in col[c] or
                    item in grid[(r//3, c//3)]):
                    return False
                
                row[r].add(item)
                col[c].add(item)
                grid[(r//3, c//3)].add(item)

        return True

        """                
        #Row check
        for row in range(9):
            r = set()
            for col in range(9):
                if board[row][col] in r:
                    return False
                elif board[row][col] != ".":
                    r.add(board[row][col])

        #Column check
        for row in range(9):
            c = set()
            for col in range(9):
                if board[col][row] in c:
                    return False
                elif board[col][row] != ".":
                    c.add(board[col][row])

        #Grid Check
        start =[ (0,0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]

        for i,j in start:
            grid = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    items = board[row][col]
                    if items in grid:
                        return False
                    elif items != ".":
                        grid.add(items)
        return True
        """