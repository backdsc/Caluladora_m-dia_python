nome = input("Informe seu nome: ")
serie = input("Informe a sua serie: ")
sala = input("Informe sua sala: ")
nota1 = float(input("Informe sua nota da primeira unidade: "))
nota2 = float(input("Informe sua nota da segunda unidade: "))
nota3 = float(input("Informe sua nota da segunda unidade: "))


total = float((nota1 + nota2 + nota3) / 3)

if (total < 7):
    print("O aluno foi reprovado")
elif(total < 6):
    print("O aluno está de recuperação!")
else:
    print("O aluno está aprovado!")

print(nome, serie, sala, "Sua média foi", total) 