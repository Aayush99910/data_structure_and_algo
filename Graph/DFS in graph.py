G = [
  [0, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0]
]

visited_vertices = set()
ROW = len(G)
COL = len(G[0])

def dfs(rowIndex, colIndex, grid):
  # two conditions 
  # One condition consists of multiple conditions 
    # If we are out of bounds 
    # If the cell's value is 1
    # If we have already visited a vertex 
  
  # Another condition consists of when we reach the bottom left 
  if (min(rowIndex, colIndex) < 0 or rowIndex == ROW or colIndex == COL or grid[rowIndex][colIndex] == 1 or (rowIndex, colIndex) in visited_vertices):
    return 0 
  if (rowIndex == ROW - 1 and colIndex == COL - 1):
    return 1
  
  visited_vertices.add((rowIndex, colIndex))

  no_of_path = 0
  no_of_path += dfs(rowIndex - 1, colIndex, grid) #type: ignore
  no_of_path += dfs(rowIndex + 1, colIndex, grid) #type: ignore
  no_of_path += dfs(rowIndex, colIndex - 1, grid) #type: ignore
  no_of_path += dfs(rowIndex, colIndex + 1, grid) #type: ignore

  visited_vertices.remove((rowIndex, colIndex))

  return no_of_path 
  


print(dfs(0, 0, G))