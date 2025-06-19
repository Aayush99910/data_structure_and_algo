KNIGHTS_MOVES = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [2, 1]] # these are the moves that knight can go from (0,0)
KNIGHTS_MOVES_1 = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def print_board(board): 
    for row in board: 
        for col in row:
            print("{0:>2d}".format(col), end=" ")
        print() 
    print()

def knights_tour(n, row, col):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[row][col] = 0 
    
    def backtrack(board, row, col, move_no):
        # base case if we are out of the grid
        if (len(board) * len(board) == move_no):
            return True 

        # make the move
        for move in KNIGHTS_MOVES_1:
            newr, newc = row + move[0], col + move[1]

            # valid move
            if min(newr, newc) < 0 or newr >= len(board) or newc >= len(board[0]) or board[newr][newc] != -1:
                continue 

            # this is valid move
            board[newr][newc] = move_no 

            # call backtacking from this part and check to see if there is a soltuion
            if backtrack(board, newr, newc, move_no + 1):
                return True 

            # backtrack and go find other solution
            board[newr][newc] = -1

        
        # this is not working
        return False 
    
    backtrack(board, 0, 0, 1)
    return board

print_board(knights_tour(5, 0, 0))

    


# # n and a start row and start col 
# def knights_tour(n, r, c):
#     board = [[-1 for _ in range(n)] for _ in range(n)]
#     board[r][c] = 0

#     def backtracking_knight(row, col, move_count):
#         # base case 
#         if  move_count == (len(board[row]) * len(board[col])):
#             return True 

#         for move in KNIGHTS_MOVES_1:
#             newr, newc = row + move[0], col + move[1]

#             if min(newr, newc) < 0 or newr >= len(board) or newc >= len(board[0]) or board[newr][newc] != -1:
#                 continue    
            
#             board[newr][newc] = move_count 

#             if backtracking_knight(newr, newc, move_count + 1):
#                 return True 

#             board[newr][newc] = -1

        
#         return False 
    

#     backtracking_knight(r, c, 1)
#     return board

# print_board(knights_tour(5, 0, 0))


