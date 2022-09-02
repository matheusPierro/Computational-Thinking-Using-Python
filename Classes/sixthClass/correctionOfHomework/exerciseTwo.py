a = float(input("Primeiro lado: "))
b = float(input("Segundo Lado: "))
c = float(input("Terceiro lado: "))

if (a == b) and (a == c):
    print("Equilátero")
elif(a == b) or (a == c) or (b == c):
    print("Isósceles")
else:
    print("Escaleno")