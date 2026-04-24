horas_normais = float(input("Digite as horas normais trabalhadas: "))
horas_extras = float(input("Digite as horas extras trabalhadas: "))

# cálculo do salário bruto
salario_bruto = (horas_normais * 10) + (horas_extras * 15)

# desconto de 10%
salario_liquido = salario_bruto * 0.90

print("\nSalário bruto: R$ {:.2f}".format(salario_bruto))
print("Salário líquido: R$ {:.2f}".format(salario_liquido))