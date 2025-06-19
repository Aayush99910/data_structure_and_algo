class Solution:
    def solveNQueens(self, n: int):
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def solveNQueensRecursive(board, cols, leftDiagonals, rightDiagonals, row, result):
            # base case 
            if row >= len(board):
                result.append(["".join(r) for r in board])
                return 
            
            for col in range(len(board)):
                if col in cols or (row - col) in leftDiagonals or (row + col) in rightDiagonals:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                leftDiagonals.add(row - col)
                rightDiagonals.add(row + col)

                solveNQueensRecursive(board, cols, leftDiagonals, rightDiagonals, row + 1, result)

                board[row][col] = "."
                cols.remove(col)
                leftDiagonals.remove(row - col)
                rightDiagonals.remove(row + col)
                
            
        solveNQueensRecursive(board, set(), set(), set(), 0, res)
        return res
    

s = Solution()
print(s.solveNQueens(4))