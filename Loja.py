funcionario1 = str.upper(input("funcionario 1 : "))
totalVendas1 = int (input("Digite o total de vendas: "))
funcionario2 = str.upper(input("funcionario 2 : "))
totalVendas2 = int (input("Digite o total de vendas: "))

if (totalVendas1 > totalVendas2):
    bonus = totalVendas1*0.05
    vencedor = funcionario1
else:
    bonus = totalVendas2*0.05
    vencedor= funcionario2
print ("o funcionario ",vencedor, "venceu e ganhou " , bonus, "reais de bônus!")

    





