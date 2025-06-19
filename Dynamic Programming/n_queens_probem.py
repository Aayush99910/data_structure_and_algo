import copy 

# You are given a length of a number n then you have to find a solution 
# for how many queens can you place in the board and return true or false
# you will be referencing the same board through out the whole algorithm
def is_valid_spot(board, row, col):
    # this function will help to see if this is a valid position
    # checks all the col 
    for i in range(row):
        if board[i][col] == 1:
            return False 
    

    # checks every left and right diagonal
    # left
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False 
        
        i -= 1
        j -= 1

    
    # right 
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False 
        
        i -= 1
        j += 1

    return True 


# so now we will have the function that can be called for our n_queens
def n_queens_recursive(board, start, result):
    # base case
    # we have reached out of the board 
    if start >= len(board):
        result.append(copy.deepcopy(board))
        return

    # now repitatibve case 
    for col in range(len(board[0])):
        # see if you can place the queen
        if is_valid_spot(board, start, col):
            # visit this board
            board[start][col] = 1 
            
            # calling the n queens recursive function with new row
            n_queens_recursive(board, start + 1, result)

            # if there was no match then we backtrack
            board[start][col] = 0


    return False

def n_queens(n):
    # Create a board of size n x n and initialize all cells with 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []

    # Call the recursive function, starting at row 0
    n_queens_recursive(board, 0, result)    
    print(result)

n_queens(9)
        
