class Solution:
    def checkValidGrid(self, grid):
        n = len(grid)
        if grid[0][0] != 0:
            return False 
        
        def search(g, row, col, move_no): 
            if g[row][col] == (n * n) - 1:
                return True
            
            knights_move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
            for move in knights_move:
                newr, newc = row + move[0], col + move[1]

                if min(newr, newc) < 0 or newr >= len(g) or newc >= len(g[0]) or g[newr][newc] != move_no: 
                    continue 

                if search(g, newr, newc, move_no + 1):
                    return True 
                

            return False 

        return search(grid, 0, 0, 1)
    
s = Solution()
print(s.checkValidGrid([[0,3,6],[5,8,1],[2,7,4]]))
