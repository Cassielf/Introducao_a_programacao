PaoDeQueijo = 12
Cookie = 20
PrecoPaoDeQueijo = 6.79
PrecoCookie = 11.34

comida = str.lower (input("Qual comida você pretende comprar? "))
pessoas = int (input("Quantas pessoas você convidou? "))

if (comida == "pão de queijo"):
    if (pessoas%12 != 0):
        pacoteresto = 1
    else:
        pacoteresto = 0

    pacoteQueijo = pessoas//PaoDeQueijo
    pacotetotal = pacoteQueijo+pacoteresto
    compra = PrecoPaoDeQueijo*pacotetotal
    
elif (comida == "cookie"):
    if (pessoas%20 != 0):
        pacoteresto=1
    else:
        pacoteresto=0
        
    pacoteCookie = pessoas//Cookie
    pacotetotal = pacoteCookie+pacoteresto
    compra = PrecoCookie*pacotetotal

print ("o valor total será de R$ {0} ".format(compra))
