precoLivro = float(input("Digite o preço do livro: "))

if(precoLivro <= 10.00):
    desconto = precoLivro * 0.08
elif(precoLivro <= 60.00):
    desconto = precoLivro * 0.10
else:
    desconto = precoLivro * 0.2

print(desconto)