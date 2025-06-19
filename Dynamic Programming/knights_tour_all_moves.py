import copy

KNIGHTS_MOVES = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]



def knight_move(board, row, col, move_no, result):
    # base case 
    if move_no == len(board) ** 2:
        result.append(copy.deepcopy(board))
        

    for move in KNIGHTS_MOVES:
        newr, newc = row + move[0], col + move[1]
        if min(newr, newc) < 0 or newr >= len(board) or newc >= len(board[0]) or board[newr][newc] > -1: 
            continue 
            
        board[newr][newc] = move_no
        knight_move(board, newr, newc, move_no + 1, result)
        board[newr][newc] = -1
    

def knight_move_call(n, result):
    board = [[-1 for _ in range(n)] for _ in range(n)] 
    board[0][0] = 0
    knight_move(board, 0, 0, 1, result)

res = []
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
knight_move_call(5, res)
