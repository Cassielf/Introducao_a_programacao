encomendaBrigadeiro = int (input("digite aqui a quantidade de brigadeiros: "))
encomendaCajuzinho = int (input("digite aqui a quantidade de cajuzinho: "))
convidados = int (input("digite aqui a quantidade de crianças convidadas: "))
brigadeiro = 0.90
cajuzinho = 0.70
valorTotal = (encomendaBrigadeiro*brigadeiro)+(encomendaCajuzinho*cajuzinho)
docesPorCrianca = (encomendaBrigadeiro+encomendaCajuzinho)//convidados

print ("o valor total dos doces é %.2f"%valorTotal," reais, e cada criança poderá comer", docesPorCrianca,"doces.") 
