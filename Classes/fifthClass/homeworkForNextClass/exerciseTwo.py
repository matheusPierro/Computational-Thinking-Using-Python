base = int(input("Digite o valor da base do triângulo: "))
ladoUmDoTriangulo = int(input("Digite o valor do lado 2 do triângulo: "))
LadoDoisDoTriangulo = int(input("Digite o valor do lado 3 do triângulo: "))

if (ladoUmDoTriangulo == LadoDoisDoTriangulo != base):
    print("Triângulo isósceles")

elif (ladoUmDoTriangulo == LadoDoisDoTriangulo == base):
    print("Triângulo equilatero")

elif (ladoUmDoTriangulo != LadoDoisDoTriangulo != base):
    print("Triângulo escaleno")