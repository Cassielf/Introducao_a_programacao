plastico300 = 5.10
plastico500 = 9.20
aluminio300 = 10
aluminio500 = 14.50


tipoGarrafa = str.lower(input("Qual o tipo de garrafa que você deseja? "))
volume = int(input("Qual o volume da garrafa que você quer? "))
quantidade=int(input("Digite a quantidade de garrafas: "))

if(tipoGarrafa == "plástico")or(tipoGarrafa == "plastico"):
    if(volume == 300):
        pagamento = plastico300*quantidade
    else:
        pagamento = plastico500*quantidade
            
elif (tipoGarrafa == "alumínio") or (tipoGarrafa == "aluminio"):
    if (volume == 300):
        pagamento = aluminio300*quantidade
    else:
        pagamento = aluminio500*quantidade

if (quantidade >= 3):
    pagamento = pagamento*0.9
    print ("Você ganhou 10% de desconto!")
else:
    pagamento = pagamento

print ("O valor total da compra é de R$ {0}".format(pagamento))
            

