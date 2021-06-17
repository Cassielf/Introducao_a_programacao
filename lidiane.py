valorProduto = int(input ("Digite aqui o valor do produto: "))
valorPagamento = int (input("Digite aqui quanto o cliente pagou: "))
troco = valorPagamento - valorProduto

trocoEntregue5 = (troco // 5)
trocoEntregue2 = (troco // 2)
trocoEntregue1 = (troco // 1)

print ("o troco é " , troco, "e pode ser entregue em: ", trocoEntregue5, "cédulas de 5, ou ", trocoEntregue2, "cédulas de 2, ou", trocoEntregue1, " moedas.")
