diasAno = 365
diasMes = 30
diasSemana = 7

totalDias = int (input ("qual a quantidade de dias já vividos? "))#informe que o tipo de dado a ser recebido é inteiro

quantAnos = totalDias//diasAno #considere usar a // para retornar uma divisão inteira

quantMeses = totalDias//diasMes #o nome da variável para realizar a divisao estava incorreto pois estava diames ao invés de diaMes (m maiúsculo);
#é recomendável utilizar // para divisão inteira.

quantSemanas = totalDias//diasSemana #diasSemana precisa ser informado para fazer o cálculo;
#para calcular a quantidade de semanas use o total de dias dividido pela semana e assim retornará a quantidade correta de semanas que o usuário viveu;
#é recomendável utilizar // para que seja feira uma divisão inteira

print ("você viveu aproximadamente", quantAnos, "anos")

print ("você viveu aproximadamente {} meses".format (quantMeses)) #para utilizar o metodo format deve ser usado o ponto antes da palavra format, exemplo: (.format(variável))

print ("você viveu aproximadamente {s} semanas".format(s=quantSemanas))#para utilizar o metodo format deve ser usado o ponto antes da palavra format, exemplo: (.format(variável))
