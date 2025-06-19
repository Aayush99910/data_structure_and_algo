import heapq
from collections import defaultdict

class Graph: 
  def __init__(self, vertices):
    self.V = vertices
    self.graph = defaultdict(list)

  def add_edge(self, v, u, w):
    self.graph[u].append((v, w))
    self.graph[v].append((u, w))

  def prim_mst(self):
    mst_set = set() 
    result = []
    edge_list = []
    total_weight = 0.0 
    start_vertex = 0 
    mst_set.add(start_vertex)
    
    for vertex, weight in self.graph[start_vertex]:
      heapq.heappush(edge_list, (weight, start_vertex, vertex))
    
    while len(mst_set) < self.V:
      weight, u, v = heapq.heappop(edge_list)
      if v not in mst_set:
        mst_set.add(v)
        total_weight += weight 
        result.append((u, v, weight))

        for next_vertex, weight in self.graph[v]:
          if next_vertex not in mst_set:
            heapq.heappush(edge_list, (weight, v, next_vertex))
    
    return result, total_weight