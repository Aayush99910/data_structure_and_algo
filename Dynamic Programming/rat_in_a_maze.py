def find_path_rat_in_maze(maze, row, col, visited_cells, path, result):
    # you are starting at a wall and no more move possible
    if maze[row][col] == 0:
        return 
    
    # if we are at the destination then add the path to result and return 
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        result.append(path[:])
        return 
    
    # there is like 4 ways to go now
    # down, left right, top
    directions = {
        'D': [1, 0],
        'R': [0, 1],
        'U': [-1, 0],
        'L': [0, -1]
    }

    
    for direction, array in directions.items(): 
        newRow, newCol = array 
        newMoveRow, newMoveCol = row + newRow, col + newCol

        # check if the move is valid and check if that is also in visited cells
        if min(newMoveRow, newMoveCol) < 0 or newMoveRow == len(maze) or newMoveCol == len(maze[0]) or (newMoveRow, newMoveCol) in visited_cells:
            continue 

        # if it is valid and not in visited_celss then 
        path.append(direction)
        visited_cells.add((newMoveRow, newMoveCol))
        find_path_rat_in_maze(maze, newMoveRow, newMoveCol, visited_cells, path, result)

        # remove the path after being discovered
        path.pop()
        visited_cells.remove((newMoveRow, newMoveCol))
    


maze1 = [[1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1]]

result = []
find_path_rat_in_maze(maze1, 3, 0, set(), [], result)
print(result)

