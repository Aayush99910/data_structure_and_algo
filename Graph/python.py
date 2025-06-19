from collections import defaultdict

class Solution:
    def minMoves(self, matrix):
        ROW, COL = len(matrix), len(matrix[0])
        visited_cells = set() 
        visited_letter = set() 
        hashMap_teleportation = defaultdict(list)

        # finding all the teleportation letters
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col].isalpha():
                    hashMap_teleportation[matrix[row][col]].append((row, col))
                    
        best_move = float('inf')
        total_move = 0

        def dfs(matrix, row, col, ROW, COL, visited_cells, visited_letter, hashMap_teleportation, total_move, best_move):
            # base case check if this is the best move
            if row == ROW - 1 and col == COL - 1:
                if total_move < best_move:
                    best_move = total_move

                return  
            
            if matrix[row][col].isalpha() and matrix[row][col] not in visited_letter:
                newr1, newc1 = hashMap_teleportation[matrix[row][col]].pop()
                visited_letter.add((matrix[row][col]))
                visited_cells.add((row, col))
                visited_cells.add((newr1, newc1))
                dfs(matrix, newr1, newc1, ROW, COL, visited_cells, visited_letter, hashMap_teleportation, total_move, best_move)
                visited_letter.remove((matrix[row][col]))
                visited_cells.add((row, col))
                visited_cells.remove((newr1, newc1))
            else:
                moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
                for move in moves:
                    newr, newc = row + move[0], col + move[1]
                    if min(newr, newc) < 0 or newr >= ROW or newc >= COL or matrix[newr][newc] == "#" or (newr, newc) in visited_cells:
                        continue 

                    total_move += 1
                    visited_cells.add((newr, newc))
                    dfs(matrix, newr, newc, ROW, COL, visited_cells, visited_letter, hashMap_teleportation, total_move, best_move)
                    total_move -= 1
                    visited_cells.remove((newr, newc))

        visited_cells.add((0, 0))
        dfs(matrix, 0, 0, ROW, COL, visited_cells, visited_letter, hashMap_teleportation, total_move, best_move)
        
        if best_move == float('inf'):
            return -1
        
        return best_move
                
                

s = Solution()
print(s.minMoves(["A..",".A.","..."]))