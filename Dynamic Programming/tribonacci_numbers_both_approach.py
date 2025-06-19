from collections import deque

def tribonacci_top_down(n, memo):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    if n == 2:
        return 1
    
    memo[n] = tribonacci_top_down(n - 1, memo) + tribonacci_top_down(n - 2, memo) + tribonacci_top_down(n - 3, memo)
    return memo[n]


def tribonacci_bottom_up(n):
    if n <= 1:
        return n 
    
    if n == 2:
        return 1
    
    tab = [0] * (n + 1)
    tab[0] = 0 
    tab[1] = 1
    tab[2] = 1 

    for i in range(3, n + 1):
        tab[i] = tab[i - 3]  + tab[i - 2] + tab[i - 1]
    
    return tab[n]

def tribonacci_bottom_up_best_approach(n):
    if n <= 1:
        return n 
    
    if n == 2:
        return 1
    
    queue = deque(maxlen=3)
    queue.extend([0, 1, 1])

    for _ in range(3, n + 1):
        queue.append(sum(queue))

    return queue.pop()


print(tribonacci_top_down(40, {}))
print(tribonacci_bottom_up(40))
print(tribonacci_bottom_up_best_approach(40))


class Solution:        
    def climbStairs(self, n: int) -> int:
        def calculate(n):
            if n <= 3:
                return n

            m = [0] * n
            m[0] = 1
            m[1] = 2
            m[2] = 3
            
            for i in range(3, n):
                m[i] = m[i - 1] + m[i - 2]
            
            return m[n - 1]
        
        return calculate(n)

        
        
        
        
        
s = Solution()
s.climbStairs(4)