buenosairesP = 810
buenosairesH = 220
santiagoP = 900.50
santiagoH = 307.50
montevideoP = 780
montevideoH = 280.60


cidade = str.upper(input("Qual a cidade que você pretende viajar? "))
dias = int (input("Quantos dias você pretende passar? "))

if (cidade== "BUENOS AIRES"):
    passagem = buenosairesP*2
    hospedagem = buenosairesH*dias
elif (cidade == "SANTIAGO"):
    passagem = santiagoP*2
    hospedagem = santiagoH*dias
elif (cidade == "MONTEVIDEO"):
    passagem = montevideoP*2
    hospedagem = montevideoH*dias

total = passagem+hospedagem

print ("Sua viagem custará R$ %0.2f"%total)
    
