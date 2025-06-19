def coin_change_memoization(coins, index, total_sum, memo): 
    # first thing is if the index or the total sum is less than 0 there is no other way
    if index < 0 or total_sum < 0:
        return 0
    
    # there is another way that is if the total_sum is 0 that means we found our path
    if total_sum == 0:
        return 1 
    # if this combination has not been explored before then we can explore this
    elif memo[index][total_sum] == -1:
        # this is very interesting 
        # this is also confusing 
        # in the first function call we are USING that coin and subtracting sum from 
        # total sum 
        # in the second function call we are SKIPPING that coin and going from next smallest 
        # coin
        memo[index][total_sum] = coin_change_memoization(coins, index, total_sum - coins[index], memo) + coin_change_memoization(coins, index - 1, total_sum, memo)

    return memo[index][total_sum]

coins = [1, 2]
target = 4
memo = [[-1 for _ in range(target +  1)] for _ in coins]
print(coin_change_memoization(coins, len(coins) - 1, target, memo))



def coin_change_tabulation(coins, target):
    memo = [[0 for _ in range(target +  1)] for _ in coins]

    memo[]
    