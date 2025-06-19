def path_at_least_k(graph, source, k, visited_set):
    if k <= 0:
        return True 
      
    visited_set[source] = True 
    for neighbor, distance in graph[source].items():
        # if neighbor is alreay visited then skip if not then do all these
        if visited_set[neighbor]:
            continue 

        k = k - distance 

        if path_at_least_k(graph, neighbor, k, visited_set):
            return True 
        
        k = k + distance
        visited_set[neighbor] = False 

    return False 

graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 3: 7, 5: 4, 8: 2},
    3: {2: 7, 4: 9, 5: 14},
    4: {3: 9, 5: 10},
    5: {2: 4, 3: 14, 4: 10, 6: 2},
    6: {5: 2, 7: 1, 8: 6},
    7: {0: 8, 1: 11, 6: 1, 8: 7},
    8: {2: 2, 6: 6, 7: 7}
}

visited_set = {vertex: False for vertex in graph}
print(path_at_least_k(graph, 0, 60, visited_set))