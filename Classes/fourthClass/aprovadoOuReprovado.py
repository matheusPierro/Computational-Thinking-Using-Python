av1 = input("Digite a primeira avaliação: ")
av1 = float(av1)
av2 = input("Digite a segunda avaliação: ")
av2= float(av2)
av3 = input("Digite a terceira avaliação: ")
av3 = float(av3)

media = (av1+av2+av3)/3

if media >= 6:
    print(f"O aluno está aprovado com média {media:.2f}")
else:
    print(f"O aluno está reprovado com média {media:.2f}")