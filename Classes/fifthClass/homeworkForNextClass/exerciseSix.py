peso = float(input("Digite seu peso em kilos: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)

if(imc <= 18.5):
    print("Abaixo do peso")
elif(imc > 18.5 and imc <= 24.9):
    print("Peso ideal")
else:
    print("Acima do peso")
