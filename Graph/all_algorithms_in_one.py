import heapq
from collections import defaultdict
from queue import PriorityQueue

class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [] 
    
    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def find(self, parent, i):
        if (parent[i] == i):
            return i 

        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y  
        elif rank[root_y] < rank[root_x]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        # initialize result, mst set, weight
        result = []
        total_weight = 0 
        parent = []
        rank = []

        # sort the graph
        self.graph = sorted(self.graph, key=lambda x: x[2])
        
        # add nodes to parent
        # and everyone's rank will be 0 for now
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # maintain an index and edge count
        i = 0
        e = 0

        # do it while e < len(graph) - 1
        while e < self.V - 1:
            u, v, weight = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # compare roots if same root then dont add 
            # if different roots then add it
            if x != y: 
                result.append((u, v, weight))
                e += 1
                total_weight += weight 
                self.union(parent, rank, x, y)
        
        return result, total_weight
    

class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        mst_set = set() 
        edge_list = []
        result = []
        start_vertex = 0
        total_weight = 0
        mst_set.add(start_vertex)

        for v, w in self.graph[start_vertex]:
            heapq.heappush(edge_list, (w, start_vertex, v))

        while len(mst_set) < self.V:
            weight, u, v = heapq.heappop(edge_list)
            
            if v not in mst_set:
                mst_set.add(v)
                result.append((u, v, weight))
                total_weight += weight
                for next_vertex, weight in self.graph[v]:
                    if next_vertex not in mst_set:
                        heapq.heappush(edge_list, (weight, v, next_vertex))
        
        return result, total_weight
    
def dijstra(graph, start_vertex):
    # initialize all the things
    paths = {vertex: [] for vertex in graph}
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    paths[start_vertex] = [start_vertex]

    priority_queue  = PriorityQueue()
    priority_queue.put((0, start_vertex))

    while not priority_queue :
        current_distance, current_vertex = priority_queue.get() # type:ignore

        if current_distance > distances[current_vertex]:
            continue 
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance 
                priority_queue.put((distance, neighbor))
                paths[neighbor] = paths[current_vertex] + [neighbor]

    return distances, paths 

def bellmanford_algorithm(graph, start_vertex):
    # initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start_vertex] = 0

    for _ in range(len(graph)):
        updated = False 
        for u in graph:
            for v, w in graph[u].items():
                if w + distances[u] < distances[v]:
                    distances[v] = w + distances[u]
                    predecessors[v] = u 
                    updated = True 

        if not updated:
            break 

    # check for cycle
    for u in graph:
        for v, w in graph[u].items():
            if w + distances[u] < distances[v]:
                print("Negative cycle")
                return None, None  



    
    
    




        

    