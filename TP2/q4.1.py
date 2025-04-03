def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# Testes
for i in range(6):
    print(f"{i}! = {fatorial(i)}")

