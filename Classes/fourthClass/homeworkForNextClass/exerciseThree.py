valorMercadoria = float(input("Qual o valor da mercadoria? "))
valorUsuario = float(input("Qual valor o usuário tem em mãos? "))

if(valorUsuario >= valorMercadoria):
    print("O valor que o usuário tem é suficiente para comprar a mercadoria")
else:
    print("O valor que o usuário tem não é suficiente para comprar a mercadoria")