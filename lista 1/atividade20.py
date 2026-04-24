import math

qtd_blusas = int(input("Digite a quantidade de blusas: "))

metros_necessarios = qtd_blusas * 120

novelos = math.ceil(metros_necessarios / 125)

print("Quantidade de novelos necessários:", novelos)