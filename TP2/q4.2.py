import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci otimizado (memorização)
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]

# Testes
n = 35
start = time.time()
print(f"Fibonacci({n}) = {fibonacci(n)} (Sem Memo) - Tempo: {time.time() - start:.5f}s")

start = time.time()
print(f"Fibonacci({n}) = {fibonacci_memo(n)} (Com Memo) - Tempo: {time.time() - start:.5f}s")

