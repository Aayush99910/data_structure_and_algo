from queue import PriorityQueue

# algorithm
def dijkstra_paths(graph, starting_point):
  # define empty path dictionary, empty distances dictionary
  paths = {vertex: [] for vertex in graph}
  distances = {vertex: float('inf') for vertex in graph}
  queue = PriorityQueue()

  # we need to add the first starting point to the paths, distances and queue 
  paths[starting_point] = [starting_point]
  distances[starting_point] = 0
  queue.put((0, starting_point))

  # our main algorithm which will loop until the queue is empty
  # it will get the lowest minimum (tuple) (distance, vertex)
  # we will see if the distance is greater than in the distances dictionary 
  # if it is then ignore
  # else we need to calculate the total distance
  # update distances dictionary
  # add it to the queue
  # update path
  while not queue.empty():
    cd, cv = queue.get()

    if cd > distances[cv]:
      continue 
      
    for n, w in graph[cv].items():
      td = cd + w 

      if td < distances[n]:
        distances[n] = td 
        queue.put((td, n))
        paths[n] = paths[cv] + [n]

    
  return paths

def two_leg_path(graph, start, via, target):
  start_to_all_vertices =  dijkstra_paths(graph, start)
  
  if via in start_to_all_vertices[target]:
    return start_to_all_vertices[target]

  path_from_start_to_via = start_to_all_vertices[via]

  via_to_all_vertices = dijkstra_paths(graph, via)
  path_from_via_to_target = via_to_all_vertices[target]

  first_leg = path_from_start_to_via
  second_leg = path_from_via_to_target

  if not (first_leg or second_leg):
    return []
    
  combined_path = first_leg[:-1] + second_leg
  return combined_path



# Define the graph
graph = {
  'Moololaba': {'Nambour': 54},
  'Seymore': {'Lismore': 4},
  'Lismore': {'Moololaba': 22},
  'Oodnadatta': {'Tullamore': 13, 'Lismore': 129},
  'Nambour': {'Maroochydore': 8},
  'Tullamore': {'Maroochydore': 2, 'Seymore': 4, 'Moololaba': 125},
  'Maroochydore': {'Seymore': 56}
}

# Find the shortest paths
# paths = dijkstra_paths(graph, "Oodnadatta")

# # Print the results
# for town, path in paths.items():
#     print(town, ":", path)

print(two_leg_path(graph, "Oodnadatta", "Seymore", "Maroochydore"))