dias = int(input("Digite a quantidade de dias: "))

anos = dias // 360
resto = dias % 360

meses = resto // 30
dias_restantes = resto % 30

print("Tempo sem acidentes:")
print(anos, "ano(s),", meses, "mes(es) e", dias_restantes, "dia(s)")

 #"dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

# Cálculo de anos, meses e dias
#anos = dias_trabalhados // 365
#meses = (dias_trabalhados % 365) // 30
#dias = (dias_trabalhados % 365) % 30

# Exibição do resultado
#print(f"{dias_trabalhados} dias equivalem a {anos} anos, {meses} meses e {dias} dias.")"