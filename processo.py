quantMinutos = int (input ("Digite aqui quantos minutos foram levados para analisar cada processo: "))
expediente = 8 * 60 #conversão de horas para minutos
quantProcesso = expediente//quantMinutos

print ("Foram revisados", quantProcesso, "processos.")
