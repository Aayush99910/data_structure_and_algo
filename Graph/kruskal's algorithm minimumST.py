class Graph: 
  # Initialize the graph with the number of vertices and an empty list of edges
  def __init__(self, vertices):
    self.V = vertices 
    self.graph = []

  # Add an edge to the graph
  def add_edge(self, u, v, w):
    # append the edge to the graph with the source, destination, and weight
    self.graph.append((u, v, w))

  # Find the parent of a node
  def find(self, parent, i):
    if parent[i] == i:
      return i
    return self.find(parent, parent[i])

  # Union two sets: x and y
  def union(self, parent, rank, x, y):
    # Find the root of the sets
    root_x = self.find(parent, x)
    root_y = self.find(parent, y)
        
    # Union the sets by rank
    if rank[root_x] < rank[root_y]:
      parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
      parent[root_y] = root_x
    else:
      parent[root_y] = root_x
      rank[root_x] += 1

  # kruskal's algorithm to find the minimum spanning tree
  def kruskal_mst(self):
    result = [] 

    self.graph = sorted(self.graph, key = lambda x: x[2])

    parent = [] 
    rank = []

    for i in range(len(self.graph)): 
      parent.append(i)
      rank.append(0)

    e, i = 0, 0
    total_weight = 0.0

    while e < self.V - 1 and i < len(self.graph):
      u, v, w = self.graph[i]
      x = self.find(parent, u)
      y = self.find(parent, v)

      if x != y:
        e += 1
        result.append((u, v, w))
        total_weight += w 
        self.union(parent, rank, x, y)
      
      i += 1

    return result, total_weight

    
# driver code
g = Graph(8)
edges = [
    (2, 1, 0.09), (0, 6, 0.11), (4, 2, 0.11), (1, 7, 0.15),
    (6, 5, 0.19), (6, 3, 0.20), (4, 1, 0.24), (5, 4, 0.25),
    (0, 7, 0.28), (5, 3, 0.31), (0, 5, 0.32), (4, 3, 0.35),
    (2, 3, 0.42), (4, 7, 0.45), (5, 2, 0.51), (6, 7, 0.54),
    (0, 4, 0.71)
]
for u, v, w in edges:
    g.add_edge(u, v, w)
mst, total_weight = g.kruskal_mst()
print("The minimum total weight:", total_weight)
print("The minimum spanning tree:", mst)