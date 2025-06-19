def minimum_cost_path(board, row, col, memo):
    # base case would be that if the row and col is out of bound or 
    # we have reached the 0,0 point
    if min(row, col) < 0:
        return float('inf')
    
    if row == 0 and col == 0:
        return board[row][col]
    
    if memo[row][col] != -1:
        return memo[row][col]
    
    # store this path
    memo[row][col] = min(minimum_cost_path(board, row, col - 1, memo), minimum_cost_path(board, row - 1, col, memo), minimum_cost_path(board, row - 1, col - 1, memo)) + board[row][col]
    return memo[row][col]

board = [[5, 8, 6], [3, 2, 4], [1, 7, 9]]
n = len(board) # row
m = len(board[0]) # col
memo1 = [[-1 for _ in range(m)] for _ in range(n)] 
print(minimum_cost_path(board, 2, 2, memo1))


def minimum_cost_path_tab(board, row, col):
    # making a tab array that has cost
    tab = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    # starting position is filled with the the cost
    tab[0][0] = board[0][0]

    # now building the solution
    # for that whole column we need to put the cost as cost + top cell
    # this will be the same because when we are in the left most column the only cost that we can have it from top cell
    # same is true for upper most row  as well
    for i in range(1, len(board)):
        tab[i][0] = board[i][0] + tab[i - 1][0]

    # doing this for top row
    for i in range(1, len(board[0])):
        tab[0][i] = board[0][i] + tab[0][i - 1]


    for i in range(1, len(board)):
        for j in range(1, len(board)):
            tab[i][j] = board[i][j] + min(tab[i - 1][j - 1], tab[i - 1][j], tab[i][j - 1])

    return tab[i][j]

print(minimum_cost_path_tab([[5, 8, 6], [3, 2, 4], [1, 7, 9]], 1, 2))
