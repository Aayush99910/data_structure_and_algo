from collections import deque

def bfs(grid):
  # initialise row and col, set data structure, queue
  ROW = len(grid)
  COL = len(grid[0])
  visited_vertices = set()
  queue = deque()

  # add (0,0) in the queue and then add it into the set as well
  visited_vertices.add((0, 0))
  queue.append((0, 0))


  # initialise the length as 0 
  length = 0 

  # iterate while the queue is not 0 
  while (queue):
    # take a snapshot of the queue and then get the row and col
    for i in range(len(queue)):
      row, col = queue.popleft() 

      # if we are at the bottom right then return the length
      if (row == ROW - 1 and col == COL - 1):
        return length

      neighbors = [[0, -1], [1, 0], [0, 1], [-1, 0]] # left, top, right, bottom
      # go to all four possible track
      for differenceRow, differenceCol in neighbors:
        newRow, newCol = row + differenceRow, col + differenceCol
        # if it is not valid then skip
        if (min(newRow, newCol) < 0 or newRow == ROW or newCol == COL or grid[newRow][newCol] == 1 or (newRow, newCol) in visited_vertices):
          continue
        # if it is valid then add that track to the queue and also in the set
        queue.append((newRow, newCol))
        visited_vertices.add((newRow, newCol))

    # increase the length 
    length += 1

G = [
  [0, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0]
]

print(bfs(G))