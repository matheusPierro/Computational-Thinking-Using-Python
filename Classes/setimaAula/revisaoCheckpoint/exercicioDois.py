numeroMacas = int(input("Digite o número de maçãs compradas: "))

menorQueDoze = numeroMacas * 1.30
dozeOuMais = numeroMacas

if (numeroMacas < 12):
    print(f"O custo das suas maças foi de R${menorQueDoze:.2}")
else:
    print("O custo das suas maça foi de R$", dozeOuMais)