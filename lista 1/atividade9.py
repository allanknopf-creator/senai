qtd_pequena = int(input("Quantidade de camisetas pequenas: "))
qtd_media = int(input("Quantidade de camisetas médias: "))
qtd_grande = int(input("Quantidade de camisetas grandes: "))

valor_total = (qtd_pequena * 10) + (qtd_media * 12) + (qtd_grande * 15)

print("Valor arrecadado: R$ {:.2f}".format(valor_total))