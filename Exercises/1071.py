X = int(input())
Y = int(input())

inicio = min(X, Y)
fim = max(X, Y)

soma_impares = sum(num for num in range(inicio+1, fim) if num % 2 != 0)
print(soma_impares)