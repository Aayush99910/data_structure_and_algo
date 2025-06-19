def bellman_ford(graph, source):
    # initialize all the variables needed
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}

    # now looping through the graph
    for _ in range(len(graph) - 1):
        updated = False 
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecessors[v] = u
                    updated = True 

        if not updated:
            break 
    
    # negative cycle 
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                print("Negative Cycle detected!!")
                return None, None  

    return distances, predecessors

graph = {
    'Seattle': {'Portland': 10, 'Newport': 25},
    'Portland': {'Sacramento': 70, 'San Francisco': 80},
    'Newport': {'Portland': 5, 'Sacramento': 60, 'San Francisco': 60},
    'Sacramento': {'San Francisco': 5, 'San Jose': 15, 'Los Angeles': 20},
    'San Francisco': {'San Jose': 5},
    'Los Angeles': {'San Diego': 10},
    'San Jose': {'San Diego': 40},
    'San Diego': {}
}

distances, predecessors = bellman_ford(graph, 'Seattle')

print("Lowest costs from Seattle:")
for vertex, distance in distances.items(): # type: ignore
    print("Distance to " + vertex + ": " + str(distance))

print("\nPredecessors for each vertex:")
for vertex, pred in predecessors.items(): # type: ignore
    print("Predecessor for " + vertex + ": " + str(pred))

