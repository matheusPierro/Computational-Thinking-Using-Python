consumo_kWh = input("Digite o consumo em kWh: ")
consumo_kWh = float(consumo_kWh)

total_conta = consumo_kWh*0.20

print(f"O total da conta para o consumo de {consumo_kWh:.2f}kWh é R${total_conta:.2f}")