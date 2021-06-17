alice= int(input ("Alice, escolha 0 ou 1? "))
bob= int(input("Bob, escolha 0 ou 1? "))
clara= int(input ("Clara, escolha 0 ou 1? "))

if (clara != bob) and (clara != alice):
    print ("Clara é a vencedora!")
elif (bob != clara) and (bob != alice):
    print ("Bob é o vencedor!")
elif (alice != bob) and (alice !=clara):
    print ("Alice é a vencedora!")
else:
    print ("EMPATE! Joguem novamente!")
