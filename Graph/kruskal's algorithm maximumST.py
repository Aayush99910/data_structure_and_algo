# Maximum Spanning tree
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = []

  def add_edge(self, u, v, w):
    self.graph.append((u, v, w))

  def find(self, parent, i):
    if parent[i] == i:
      return i
    return self.find(parent, parent[i])

  def union(self, parent, rank, x, y):
    root_x = self.find(parent, x)
    root_y = self.find(parent, y)
        
    if rank[root_x] < rank[root_y]:
      parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
       parent[root_y] = root_x
    else:
      parent[root_y] = root_x
      rank[root_x] += 1

  def kruskal_mst(self):
    result = [] 
    self.graph = sorted(self.graph, key=lambda item: item[2])        
    parent = [] 
    rank = [] 
        
    for node in range(self.V):
      parent.append(node)
      rank.append(0)
        
    i, e = len(self.graph) - 1, 0 
    total_weight = 0.0 
        
    while e < self.V - 1 and i >= 0:           
      u, v, w = self.graph[i]
      i = i - 1
      x = self.find(parent, u) 
      y = self.find(parent, v) 
            
      if x != y:
        e = e + 1
        result.append((u, v, w))
        total_weight += w
        self.union(parent, rank, x, y) 
        
    return result, total_weight


g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 3)
g.add_edge(2, 0, 2)
g.add_edge(3, 4, 3)

result, total_weight = g.kruskal_mst()
print("Edges in the Maximum Spanning Tree:", result)
print("Total weight of the Maximum Spanning Tree:", total_weight)