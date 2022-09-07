numeroAmigos = int(input("Digite quantos amigos participaram do Happy Hour: "))

qtdCerveja = int(input("Digite o número de cervejas que vocês pediram: "))
qtdPcFritas = int(input("Digite o número de porções de fritas que vocês pediram: "))
qtdPcPasteis = int(input("Digite o número de porções de pastéis que vocês pediram: "))

valorCerveja = 18.0
valorFritas = 35.0
valorPasteis = 25.0

valorTotal = (qtdCerveja * valorCerveja) + (qtdPcFritas * valorFritas) + (qtdPcPasteis * valorPasteis)
valorIndividual = valorTotal / numeroAmigos

print(f"O valor total da conta será de: R${valorTotal}. E o valor individual para cada amigo será de: R${valorIndividual}")