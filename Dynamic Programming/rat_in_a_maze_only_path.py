DIRECTIONS = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}

def find_path(row, col, maze, current_path=None):
    if current_path is None:
        current_path =  []
    
    # if we are the destination then we need to return the current path
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        return current_path 

    # mark this row and col visited 
    maze[row][col] = 0 

    # search the neighbors
    for direction, array in DIRECTIONS.items(): 
        newRow, newCol = array 
        newMoveRow, newMoveCol = row + newRow, col + newCol

        if not (min(newMoveRow, newMoveCol) < 0 or newMoveRow == len(maze) or newMoveCol == len(maze[0]) or maze[newMoveRow][newMoveCol] == 0):
            current_path.append(direction)
            result = find_path(newMoveRow, newMoveCol, maze, current_path)

            if result is not None: 
                return result 

            current_path.pop() 

    
    maze[row][col] = 1
    return None 
        


