nome = input("insira o nome do aluno:")
nota1 = float(input("insira a primeira nota:"))
nota2 = float(input("insira a segunda nota:"))
media = (nota1 + nota2) / 2
print("A média das notas é:", media)
if media >= 7:
    print("o aluno está aprovado")
else:
    print("o aluno está reprovado")