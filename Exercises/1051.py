salario = float(input())

if salario <= 2000:
    print("Isento")
    
if(salario > 2000 and salario <= 3000):
    faixa_imposto = salario - 2000
    imposto_total_1faixa = faixa_imposto * 0.08
    print(f"R$ {imposto_total_1faixa:.2f}")
    
if(salario > 3000 and salario <= 4500):
    faixa_imposto_8 = 1000 * 0.08
    faixa_imposto_18 = (salario - 3000) * 0.18
    imposto_total_2faixa = faixa_imposto_8 + faixa_imposto_18
    print(f"R$ {imposto_total_2faixa:.2f}")
    
if(salario > 4500):
    faixa_imposto_8 = 1000 * 0.08
    faixa_imposto_18 = 1500 * 0.18
    faixa_imposto_28 = (salario - 4500) * 0.28
    imposto_total_3faixa = faixa_imposto_8 + faixa_imposto_18 + faixa_imposto_28
    print(f"R$ {imposto_total_3faixa:.2f}")