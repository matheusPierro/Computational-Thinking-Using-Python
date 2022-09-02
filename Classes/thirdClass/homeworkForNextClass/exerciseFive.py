print("Digite sua idade em anos meses e dias:")

anos = input("Anos:")
anos = int(anos)

meses = input("Meses:")
meses = int(meses)

dias = input("Dias:")
dias = int(dias)

idade = (anos * 365) + (meses * 30) + dias

print("A sua idade em dias é:", idade)