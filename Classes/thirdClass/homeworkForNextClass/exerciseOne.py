# Consumo de kWh

consumo_kwh = input("Digite seu consumo em kWh:")
consumo_kwh = float(consumo_kwh)

total_conta = consumo_kwh*0.20

print(f"O total da conta para o consumo em {consumo_kwh:.2f}kWh é R$ {total_conta:.2f}")
