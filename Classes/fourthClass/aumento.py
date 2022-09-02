salario = input("Digite o salário: ")
salario = float(salario)

if salario >= 800:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.20

print(f"Novo salário: {novo_salario:.2f}")