nomeTime1 = str.lower(input("qual o nome do seu time? "))
nomeTime2 = str.lower(input("qual o nome do time adversário? "))
Pontostime1 = int (input ("digite aqui a quantidade de pontos do Time 1: "))
Pontostime2 = int (input ("digite aqui a quantidade de pontos do Time 2: "))
vencedor1 = ("O time vencedor é o {0}".format(nomeTime1))
vencedor2 = ("O time vencedor é o {0}".format(nomeTime2))

if (Pontostime1 > Pontostime2):
    print (vencedor1)
elif (Pontostime2 > Pontostime1):
    print (vencedor2)
else:
    Saldotime1 = int (input("qual é o saldo de gols do Time 1? "))
    Saldotime2 = int (input("qual é o saldo de gols do Time 2? "))
    if (Saldotime1 > Saldotime2):
        print(vencedor1)
    elif (Saldotime2 > Saldotime1):
        print(vencedor2)
    else:
        Golstime1 = int (input("quantos gols o Time 1 fez? "))
        Golstime2 = int (input("quantos gols os Time 2 fez? "))
        if (Golstime1 > Golstime2):
            print(vencedor1)
        elif (Golstime2 > Golstime1):
            print(vencedor2)
        else:
            print ("EMPATE")
            

