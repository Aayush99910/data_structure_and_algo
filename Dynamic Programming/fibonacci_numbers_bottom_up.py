# this is called tabulation
def fibonacci(n):
    if n == 1:
        return 0
    
    # we will be going from bottom to the top
    tab = [0] * (n + 1)

    # put things in the tab
    tab[0] = 0
    tab[1] = 1

    # fill it in the tab
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    
    return tab[n - 1]


print(fibonacci(4))
