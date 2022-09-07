custoFabrica = float(input("Digite o custo de fábrica do carro: "))
percentualDistribuidor = 0.28 * custoFabrica
impostos = 0.45 * custoFabrica

carroNovo = custoFabrica + impostos + percentualDistribuidor

print(f"O valor do carro novo é: {carroNovo:.2f}")

