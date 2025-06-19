# we will build up our solution from top down that means we will go from that n to the base case 
def fibboncacci(n, memo):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n

    memo[n] = fibboncacci(n - 1, memo) + fibboncacci(n - 2, memo)
    return memo[n]
