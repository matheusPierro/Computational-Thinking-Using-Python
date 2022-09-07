cadernos = int(input("Digite o número de cadernos que irá levar: "))
canetas = int(input("Digite o número de canetas que irá levar: "))
lapis = int(input("Digite o número de lápis que irá levar: "))

valorCadernos = float(input("Escreva o valor dos cadernos: "))
valorCanetas = float(input("Escreva o valor das canetas: "))
valorLapis = float(input("Escreva o valor dos lapis: "))

cadernosComDesconto = valorCadernos - (valorCadernos * 0.2)
canetasComDesconto = valorCanetas - (valorCanetas * 0.05)

valorTotal = (cadernos * cadernosComDesconto) + (canetas * canetasComDesconto) + (lapis * valorLapis)

print("O valor total de sua compra será de: R$", valorTotal)