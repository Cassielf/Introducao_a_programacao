mulheres= int (input ("quantas mulheres trabalham na empresa? "))
homens= int (input ("quantos homens trabalham na empresa? "))
vinho=10.0
panetone=8.5
qtfuncionarios= mulheres+homens
presentemulheres= mulheres*vinho
presentehomens= homens*panetone
valortotal= presentemulheres+presentehomens
valormedio= valortotal/qtfuncionarios

print ("o valor gasto com presentes foi de %.2f"% valortotal, "reais, e o valor médio gasto por funcionário é de %.2f"% valormedio, "reais.")
