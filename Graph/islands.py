from collections import deque 

class Solution:
    def islandPerimeter(self, grid):
        ROW, COL = len(grid), len(grid[0])
        visited_cells = set()
        perimeter = 0 
        queue = deque()
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0 or (row, col) in visited_cells:
                    continue 
                else:
                    queue.append((row, col))
                    visited_cells.add((row, col))

                    while queue:
                        r, c = queue.popleft()
                        visited_cells.add((r, c))
                        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]] # L, T, R, D
                        
                        # look for neighbors and count perimeter
                        for direction in directions:
                            newr, newc = r + direction[0], c + direction[1]

                            # we are going to count those only that are not explorable
                            if min(newr, newc) < 0 or newr == ROW or newc == COL or grid[newr][newc] == 0:
                                perimeter += 1
                                continue
                            
                            # if it is explorable and not in visited_cells we will explore it
                            if (newr, newc) not in visited_cells:
                                queue.append((newr, newc))

        return perimeter


s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))