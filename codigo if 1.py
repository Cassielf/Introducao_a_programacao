dia = int(input("digite o dia de pagamento"))
mes = int (input("digite o mes de pagamento"))

if (dia<=20):
    iptu= 120
    print (iptu)
elif (dia >20):
    iptu= 150
    print (iptu)
else:
    iptu = 200
    print (iptu)
