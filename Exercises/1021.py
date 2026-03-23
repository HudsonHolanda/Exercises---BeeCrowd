valor = float(input())

# Converte para centavos (inteiro)
valor = int(round(valor * 100))

n100 = valor // 10000
valor %= 10000

n50 = valor // 5000
valor %= 5000

n20 = valor // 2000
valor %= 2000

n10 = valor // 1000
valor %= 1000

n5 = valor // 500
valor %= 500

n2 = valor // 200
valor %= 200

c100 = valor // 100
valor %= 100

c50 = valor // 50
valor %= 50

c25 = valor // 25
valor %= 25

c10 = valor // 10
valor %= 10

c05 = valor // 5
valor %= 5

c01 = valor

print("NOTAS:")
print(f"{n100} nota(s) de R$ 100.00")
print(f"{n50} nota(s) de R$ 50.00")
print(f"{n20} nota(s) de R$ 20.00")
print(f"{n10} nota(s) de R$ 10.00")
print(f"{n5} nota(s) de R$ 5.00")
print(f"{n2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{c100} moeda(s) de R$ 1.00")
print(f"{c50} moeda(s) de R$ 0.50")
print(f"{c25} moeda(s) de R$ 0.25")
print(f"{c10} moeda(s) de R$ 0.10")
print(f"{c05} moeda(s) de R$ 0.05")
print(f"{c01} moeda(s) de R$ 0.01")