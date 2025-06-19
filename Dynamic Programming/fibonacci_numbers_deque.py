from collections import deque 

def fibonacci_deque(n):
    if n <= 1:
        return n
    
    queue = deque(maxlen=2)
    queue.append(0)
    queue.append(1)

    for _ in range(1, n):
        queue.append(sum(queue))

    return queue.pop()


fibonacci_deque(5)