#Se a nota for maior ou igual a 6 -> aprovados
#Se a noita for menor ou igual a 4 -> reprovado
#Se a nota for maior que 4 e menor que 6 -> recuperação 
media = input("Digite a nota do aluno: ")

media = float(media)
if media >= 7:
    print("Aluno Aprovado")
elif media <= 4:
    print("Aluno Reprovado")
else:
    print("Aluno em recuperação")
    