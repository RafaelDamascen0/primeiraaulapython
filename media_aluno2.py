bin1 = float (input("Digite a nota do primeiro bimestre do aluno"))
bin2 = float (input("Digite a nota do Segundo bimestre do aluno"))
bin3 = float (input("Digite a nota do terceiro bimestre do aluno"))
bin4 = float (input("Digite a nota do quarto bimestre do aluno"))

media = (bin1 + bin2 + bin3 + bin4)/4

media = float(media)
if media >= 7:
    print("Aluno Aprovado")
elif media <= 4:
    print("Aluno Reprovado")
else:
    print("Aluno em recuperação")



