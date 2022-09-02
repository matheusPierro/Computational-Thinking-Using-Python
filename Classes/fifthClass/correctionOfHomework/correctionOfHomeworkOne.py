blocoMorador = int(input("digite o bloco onde mora (1 a 4): "))

resto = blocoMorador % 2

if(resto == 0):
    print("Seu bloco é abastecido pela caixa da água A")
else:
    print("Seu bloco é abastecido pela caixa da água B")