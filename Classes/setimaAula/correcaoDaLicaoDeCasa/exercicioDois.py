from tabnanny import check


for cont in range(1, 16):
    check1 = float(input("Digite a nota do checkpoint 1: ")) 
    check2 = float(input("Digite a nota do checkpoint 2: ")) 
    check3 = float(input("Digite a nota do checkpoint 3: ")) 

    media = (check1 + check2 + check3) / 3

    print(f"Media: {media:.2f}")