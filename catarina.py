vendas = int(input("Quantos jogos você vendeu? "))
jogo = 39.90
bonus = 2.50
totalVendas = jogo*vendas
totalBonus = vendas*bonus
salario = (totalVendas*0.15)+ totalBonus

print ("Você faturou {v} reais".format (v=totalVendas))
print ("Seu bônus foi de {b} reais ".format (b=totalBonus))
print ("Seu salário será de {s} reais".format (s=salario))
