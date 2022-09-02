# Dolar em reais

valor_cotacao = input("Digite a cotação do dólar do dia:")
valor_cotacao = float(valor_cotacao)

valor_dolar = input("Digite o valor em dólares:")
valor_dolar = float(valor_dolar)

valor_reais = valor_cotacao*valor_dolar

print(f"O valor de {valor_dolar:.2f}U$ em reais = R${valor_reais:.2f}")