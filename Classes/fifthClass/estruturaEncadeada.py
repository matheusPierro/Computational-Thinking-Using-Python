idade = int(input("Digite a idade do competidor: "))

if(idade >= 10 and idade <= 45):
    if(idade >= 10 and idade <=15):
        print("Categoria infantil")
    if(idade >= 16 and idade <= 21):
        print("Categoria juvenil")
    if(idade >= 22 and idade <= 45):
        print("Categoria adulto")
else:
        print("Idade não permitida")