mediaAnual = float(input("Digite a média anual do aluno (0.0 a 10.0): "))

if(mediaAnual >= 6.0):
    print("Aprovado!")
elif(mediaAnual >= 3.0):
    print("Você ficou de exame!")
else:
    print("Reprovado!")