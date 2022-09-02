ano = int(input("Digite o ano: "))

if(ano >= 1000 and ano <= 2999):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não é bissexto")
else:
    print("Ano inválido")