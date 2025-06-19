def all_paths(graph, source, destination, visited_set, path, result):
    path.append(source)

    # if we find the destination we are going to add that path to the result
    if source == destination:
        result.append(path[:])
        return 
    
    # we will add this source as visited in our visited_set
    visited_set[source] = True 

    # now looping through all the neighbors and backtracking
    for vertex in graph[source]:
        if not visited_set[vertex]:
            all_paths(graph, vertex, destination, visited_set, path, result)
    visited_set[source] = False 
    path.pop()


graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

result = []
visited_set = {vertex: False for vertex in graph}
all_paths(graph, 1, 4, visited_set, [], result)
print(result)