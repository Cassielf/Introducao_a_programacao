estacionamento = 42
precoCarro = 1.75
quantidadeVeiculos = int (input("Quantos veículos serão estacionados? "))
if quantidadeVeiculos <= 42:
    rendimento = float(quantidadeVeiculos*precoCarro)
    vagasLivres = int (estacionamento-quantidadeVeiculos)
    estacionamentoCompleto = vagasLivres*1.75
    print ("seu rendimento é de %2.f"% rendimento, " reais, e ainda existem " ,vagasLivres, "vagas livres")
    print ("caso as vagas livres sejam ocupadas você terá um rendimento de %.2f"% estacionamentoCompleto, "reais a mais")
else:
    print ("não temos vagas suficientes!")




