from collections import deque

class Solution:
    def numIslands(self, grid) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque() 
        numIslands = 0 

        for r in range(ROW):
            for c in range(COL):
                # # condition if it is the last and final cell
                # if (r == ROW - 1 and c == COL - 1):
                #     return numIslands 
                
                if (int(grid[r][c]) == 1):
                    # incrementing our island value
                    numIslands += 1

                    # BFS AND ELIMINATE EVERY OTHER 1's that is connected to this 1.
                    queue.append((r, c))

                    while (queue):
                        for i in range(len(queue)):
                            row, col = queue.popleft()

                            neighbors = [[0, -1], [1, 0], [0, 1], [-1, 0]] #left, top, right, bottom

                            for differenceRow, differenceCol in neighbors: 
                                newRow = row + differenceRow
                                newCol = col + differenceCol 

                                # condition where it is out of bounds or where it is 0 we skip
                                if (min(newRow, newCol) < 0 or newRow == ROW or newCol == COL or int(grid[newRow][newCol]) == 0):
                                    continue
                                
                                grid[newRow][newCol] = "0"
                                queue.append((newRow, newCol))
                else:
                    continue

        return numIslands


s = Solution()
print(s.numIslands([["0","0","0","0","0","0","1"]]))
print(s.numIslands([["1"]]))