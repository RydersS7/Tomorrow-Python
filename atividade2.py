salario = float(input("Digite o seu salário: "))
aumento = float(input("Digite o aumento que tu quer receber: "))

valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento

print(f"\nAqui está o seu salário atualizado com o aumento: {novo_salario}")
