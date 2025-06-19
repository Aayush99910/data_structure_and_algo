from queue import PriorityQueue

def dijsktra(graph, start):
  # first thing is you need to initialize paths, distances and priority queue
  # path dictionary 
  paths = {vertex: [] for vertex in graph}
  paths[start] = [start] 

  distances = {vertex: float('inf') for vertex in graph}
  distances[start] = 0

  queue = PriorityQueue()
  queue.put((0, start))

  # the main loop 
  while not queue.empty():
    # first thing to do is get current vertex and then current distance
    cd, cv = queue.get()

    # checking if the distance is greater or less
    if cd > distances[cv]:
      continue 

    # going through the neighbors 
    for n, w in graph[cv].items():
      distance = cd + w 

      if distance < distances[n]:
        distances[n] = distance
        queue.put((distance, n))
        paths[n] = paths[cv] + [n]
  
  return distances, paths 

    
  
