Nome = input()
Salario = float(input())
Vendas = float(input())
Comissao = Vendas * 0.15
Total = Salario + Comissao
print(f"TOTAL = R$ {Total:.2f}")