mediaAnual = float(input("Digite a média anual do aluno: "))

if(mediaAnual >= 6.0 and mediaAnual <= 10):
    print("Aprovado")
elif(mediaAnual >= 3.0):
    print("Exame")
else:
    print("Reprovado")