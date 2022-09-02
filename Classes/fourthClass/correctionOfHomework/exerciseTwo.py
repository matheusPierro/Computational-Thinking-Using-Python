valor_cotacao = input("Digite a cotação do dólar do dia: ")
valor_cotacao = float(valor_cotacao)
valor_dolares = input("Digite o valor em dólares: ")
valor_dolares = float(valor_dolares)

valor_reais = valor_dolares*valor_cotacao

print(f"U${valor_dolares:.2f} em reais = R${valor_reais:.2f}")