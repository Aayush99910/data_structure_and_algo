# here we are just trying to see if there is a solution or not
def subset_sum_backtrack(numbers, target, current_sum, start): 
    # if the current_sum is equal to target then return true 
    if current_sum == target:
        return True 
    
    # if current_sum > target then return False 
    if current_sum > target: 
        return False 
    
    # explore all other path 
    for i in range(start, len(numbers)):
        current_sum += numbers[i]

        if subset_sum_backtrack(numbers, target, current_sum, i + 1):
            return True 

        current_sum -= numbers[i]

    return False  

def subset_sum(numbers, target):
    return subset_sum_backtrack(numbers, target, 0, 0)


numbers = [1, 2, 3, 4, 5]
target_sum = 8 
subset_sum(numbers, target_sum)