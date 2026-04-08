class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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