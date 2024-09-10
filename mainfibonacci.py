def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False


num = int(input("Digite um número: "))
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de fibonacci.")
else: print(f"{num} não pertence a sequência de fibonacci.")