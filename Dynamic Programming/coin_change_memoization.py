# def coin_change_memoization(coins, amount, memo):
#     # if the amount is 0 that means we found the answer 
#     # return 0
#     if amount == 0:
#         return 0 
    
#     # if the amount is in the memo then return that memo 
#     if amount in memo:
#         return memo[amount]
    
#     minimum_value = float("inf")
#     # we need to check if the amount is less than the three coins 
#     for coin in coins:
#         if coin > amount:
#             continue 
        
#         minimum_value = min(coin_change_memoization(coins, amount - coin, memo), minimum_value)
    
#     if minimum_value == float("inf"):
#         memo[amount] = float("inf")
#     else:
#         memo[amount] = 1 + minimum_value
#     return memo[amount]

# paisa = 3
# memo1 = [0] * (paisa + 1)
# print(coin_change_memoization([2], paisa, memo1))





# def coin_change_memoization(coins, amount, memo):
#     # if the amount is 0 that means we found the answer 
#     # return 0
#     if amount == 0:
#         return 0 
    
#     # if the amount is in the memo then return that memo 
#     if amount in memo:
#         return memo[amount]
    
#     minimum_value = float("inf")
#     # we need to check if the amount is less than the three coins 
#     for coin in coins:
#         if coin > amount:
#             continue 
        
#         minimum_value = min(coin_change_memoization(coins, amount - coin, memo), minimum_value)
    
#     if minimum_value == float("inf"):
#         memo[amount] = float("inf")
#     else:
#         memo[amount] = 1 + minimum_value
#     return memo[amount]

# paisa = 3
# memo1 = [0] * (paisa + 1)
# print(coin_change_memoization([2], paisa, memo1))





class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def coin_change_memoization(coins, amount, memo):
            # if the amount is 0 that means we found the answer 
            # return 0
            if amount == 0:
                return 0 
            
            # if the amount is in the memo then return that memo 
            if amount in memo:
                return memo[amount]
            
            minimum_value = float("inf")
            # we need to check if the amount is less than the three coins 
            for coin in coins:
                if coin > amount:
                    continue 
                
                res = coin_change_memoization(coins, amount - coin, memo)
                if res != -1:
                    minimum_value = min(minimum_value, res)
            
            if minimum_value == float("inf"):
                memo[amount] = -1
            else:
                memo[amount] = 1 + minimum_value

            return memo[amount]
        
        return coin_change_memoization(coins, amount, {})
    
print(Solution().coinChange([1], 0)) 