def subset_enumeration(array, current_sum, target, start, result, path):
    if current_sum == target: 
        result.append(path[:])
        return 

    if current_sum > target:
        return 
    
    # loop everysingle item in the array and then check for each array
    for i in range(start, len(array)):
        path.append(array[i])
        current_sum += array[i]

        # check if the sum becomes greater if so then exit
        if current_sum > target: 
            path.pop()
            current_sum -= array[i]
            continue 

        # backtrack every single solution
        subset_enumeration(array, current_sum, target, i + 1, result, path)

        # checked everything and now remove this particular item so it can be 
        # processed in the next loop
        path.pop()
        current_sum -= array[i]



result = []
subset_enumeration([1, 2, 3, 4, 5], 0, 8, 0, result, [])
print(result)