idade = int(input("digite a sua idade"))

if (idade<=5):
    ingresso = 10
elif(idade >= 60):
    ingresso=15
else:
    ingresso=25

print ("seu ingresso custa {0} reais".format(ingresso))
