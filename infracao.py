estacionarCalcada = 430
estacionarFaixa=580
limiteDeVelocidade = 50
velocidade=70 #a cada km excedido acima de 50km/h
celular= 830

infracao = str.lower(input("Qual tipo de infração foi cometida? "))

if (infracao =="estacionamento"):
    local = str.lower(input("O motorista estacionou na calçada ou na faixa? "))
    if (local == "calçada"):
        multa = estacionarCalcada
    elif (local == "faixa"):
        multa = estacionarFaixa
        
elif (infracao == "velocidade"):
    kms= int (input("A quantos km/hrs o veículo estava? "))
    multa = velocidade*(kms-limiteDeVelocidade)
        
else:
    multa = celular
    
print ("O motorista será multado por {0} e deverá pagar multa no valor de R$ {1}".format (infracao,multa))
