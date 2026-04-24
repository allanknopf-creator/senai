valor_total = float(input("Digite o valor total da conta: R$ "))

parte_inteira = int(valor_total // 3)

carlos = parte_inteira
andre = parte_inteira

felipe = valor_total - (carlos + andre)

print("Carlos paga: R$ {:.2f}".format(carlos))
print("André paga: R$ {:.2f}".format(andre))
print("Felipe paga: R$ {:.2f}".format(felipe))
