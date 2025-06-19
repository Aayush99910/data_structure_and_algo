def subset_sum_exists(values, index, total_sum, memo):
    # base case
    # if the total_sum is 0 then we have found it
    if total_sum == 0:
        return True 
    
    # another base case is if the total_sum is > 0 but we have ran out of numbers to use
    if total_sum > 0 and index < 0:
        return False 
    
    if memo[index][total_sum] is not None:
        return memo[index][total_sum]
    
    # if the current value is greater than total_sum then we dont need to include no point
    # if needed sum is 10 and the value is 11 it is going to be greater if we inlcude it
    elif values[index] > total_sum:
        memo[index][total_sum] = subset_sum_exists(values, index - 1, total_sum, memo)  
        return memo[index][total_sum]
    
    # now we need to backtrack 
    else: 
        memo[index][total_sum] = subset_sum_exists(values, index - 1, total_sum - values[index], memo) or subset_sum_exists(values, index - 1, total_sum, memo)
        return memo[index][total_sum]

values = [4, 5, 2, 10]
target = 9
memo = [[None for _ in range(target + 1)] for _ in range(len(values))]
result = subset_sum_exists(values, len(values) - 1, target, memo)
print("Can we make", target, "from", str(values) + "?", result)
