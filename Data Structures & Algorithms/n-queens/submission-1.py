class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiagonals = set()
        negDiagonals = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(arr) for arr in board])
                return
            
            for col in range(n):
                if (
                    (col not in cols) and
                    (row + col not in posDiagonals) and
                    (row - col not in negDiagonals)
                ):
                    board[row][col] = 'Q'
                    cols.add(col)
                    posDiagonals.add(row + col)
                    negDiagonals.add(row - col)

                    backtrack(row + 1)

                    board[row][col] = '.'
                    cols.remove(col)
                    posDiagonals.remove(row + col)
                    negDiagonals.remove(row - col)
        
        backtrack(0)
        return result





