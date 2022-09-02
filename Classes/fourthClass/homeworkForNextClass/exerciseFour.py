periodoPerm = int(input("Digite o tempo de permanência em horas: "))

valorTotal = periodoPerm * 5.00

if(valorTotal<=35.00):
    print(f"Valor total a pagar: R${valorTotal:.2f}")
else:
    print(f"Valor total a pagar: R$35.00")