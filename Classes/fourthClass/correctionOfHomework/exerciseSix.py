total_eleitores = input("Digite o número total de eleitores: ")
total_eleitores = int(total_eleitores)
qtde_votos_brancos =  input("Digite o número de votos brancos: ")
qtde_votos_brancos = int(qtde_votos_brancos)
qtde_votos_nulos =  input("Digite o número de votos nulos: ")
qtde_votos_nulos = int(qtde_votos_nulos)
qtde_votos_validos =  input("Digite o número de votos válidos: ")
qtde_votos_validos = int(qtde_votos_validos)

percent_brancos = (qtde_votos_brancos*100)/total_eleitores
percent_nulos = (qtde_votos_nulos*100)/total_eleitores
percent_validos = (qtde_votos_validos*100)/total_eleitores

print(f"Percentual de votos brancos: {percent_brancos:.2f}%")
print(f"Percentual de votos nulos: {percent_nulos:.2f}%")
print(f"Percentual de votos válidos: {percent_validos:.2f}%")