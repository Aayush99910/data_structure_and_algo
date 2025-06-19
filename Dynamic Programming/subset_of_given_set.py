def subset_calculation(superset, current_set, used_set, result):
    result.append(current_set.copy())

    # we need to go through elements that are not in 
    # superset - used_set 
    for value in superset - used_set:
        # now we need to add this value in our current_set and also in our used set
        current_set.add(value)

        # now adding it in our used set
        used_set.add(value)

        # doing backtracking for all other combination
        subset_calculation(superset, current_set, used_set.copy(), result)

        # explored all the possible solution now need to remove it 
        # so that the next value can be added
        current_set.remove(value)

result = []
current_set = set()
used_set = set()
subset_calculation({1, 2, 3}, current_set, used_set, result)
print(result)