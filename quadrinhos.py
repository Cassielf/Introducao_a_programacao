quantQuadrinhos = int (input("Quantos quadrinhos você tem? "))
quantAmigos = int (input("Para quantos amigos você irá doar os quadrinhos? "))
doacao = quantQuadrinhos//quantAmigos
sobra = quantQuadrinhos%quantAmigos

print ("serão doados ", doacao, "para cada amigo e sobraram", sobra, "quadrinhos")
