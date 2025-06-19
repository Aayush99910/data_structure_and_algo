def coin_change_tabulation(coins, amount):
    tab = [0] * (amount + 1)
    tab[0] = 0

    # two loops to go through the tab and also through coins
    for amount_needed in range(1, len(tab)):
        minimum_value =  float('inf')
        for coin in coins: 
            if coin > amount_needed: 
                continue 
            minimum_value = min(minimum_value, tab[amount_needed - coin])
        
        tab[amount_needed] = 1 + minimum_value
    
    if tab[amount] == float("inf"):
        return -1 
    
    return tab[amount]

print(coin_change_tabulation([2], 3))

