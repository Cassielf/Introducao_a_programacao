disciplina = int (input("Qual a quantidade de disciplinas você irá cursar? "))
judo = int (input ("Quantos minutos dura o treino de judô? "))
aulaIngles = int (input ("Quantos minutos dura a aula de inglês? "))
judoEingles = (judo+(aulaIngles*2))*60 #converter de minutos para segundos
horasOcupadas = 15*3600 #1 hora possui 3600 segundos
tempoDisciplina = (horasOcupadas-judoEingles)/disciplina

print ("você poderá se dedicar %d"% tempoDisciplina, "segundos por disciplina")
