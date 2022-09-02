precoDoLivro = float(input("Digite o preço do livro: "))

if(precoDoLivro <= 10.00):
    print(f"Com 8% de desconto seu livro custará: {precoDoLivro - (precoDoLivro * 0.08)}")
elif(precoDoLivro >= 10.01 and precoDoLivro <= 60.00):
    print(f"Com 8% de desconto seu livro custará: {precoDoLivro - (precoDoLivro * 0.1)}")
else:
    print(f"Com 8% de desconto seu livro custará: {precoDoLivro - (precoDoLivro * 0.2)}")