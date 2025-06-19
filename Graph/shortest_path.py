from collections import deque
from collections import defaultdict

class Solution:
    def minMoves(self, matrix):
        if matrix[0][0] == "#" or matrix[len(matrix) - 1][len(matrix[0]) - 1] == "#":
            return -1
        
        # all the necessary things
        ROW, COL = len(matrix), len(matrix[0])
        hashMap_tele = defaultdict(list)
        visited_cells = set()
        portal_letters = set() 
        moves = 0

        # I am making a queue to processs BFS
        queue = deque()
        
        # adding all starting points
        queue.append((0, 0, 0))
        visited_cells.add((0, 0))

        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col].isalpha():
                    hashMap_tele[matrix[row][col]].append((row, col))
        


        # main function logic 
        while queue: 
            r, c, moves = queue.popleft() 

            # if this is the bottom right then return 
            if r == ROW - 1 and c == COL - 1:
                return moves 

            # two conditions 
            # first is letters
            if matrix[r][c].isalpha() and matrix[r][c] not in portal_letters:
                for row, col in hashMap_tele[matrix[r][c]]:
                    if (row, col) != (r, c):
                        queue.appendleft((row, col, moves))
                        visited_cells.add((row, col))
                portal_letters.add(matrix[r][c])

            # another is "."
            # this will go in other else condition because from here we can go to another position as well
            # we are not even adding the "#" in our thing soo no need to check for that as we will never land on that
            directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            for direction in directions: 
                newr, newc = r + direction[0], c + direction[1]

                # check if this is a wall if this is within bounds and also if it is in visited cells
                if min(newr, newc) < 0 or newr == ROW or newc == COL or (newr, newc) in visited_cells or matrix[newr][newc] == "#":
                    continue 
                
                queue.append((newr, newc, moves + 1))
                visited_cells.add((newr, newc))

        return -1
    
s = Solution()
print(s.minMoves(matrix = ["..C.",
                           "C.A."]))



