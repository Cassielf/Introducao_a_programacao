dias= int(input("voce alugou o carro por quantos dias? "))
km= float (input ("quantos quilometros foram percorridos? "))
extra = 12
diaria = 90

if (km>100):
    pagamento = (km-100)*extra+diaria*dias
else:
    pagamento = diaria*dias

print ("o valor total a ser pago é de R$ %.2f"%pagamento)
