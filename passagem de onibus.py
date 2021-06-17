destino = str.lower(input("Qual o seu destino? "))
turno = str.lower (input("Qual o turno que você pretende viajar? "))

areiaDiurno = 19
areiaNoturno = 24
pilarDiurno = 22
pilarNoturno = 26

if (destino == "pilar"):
    if (turno == "diurno"):
        pagamento = pilarDiurno
    else:
        pagamento = pilarNoturno
    idade = int(input ("qual a sua idade? "))
    if (idade < 10) or (idade > 60):
        pagamento/=2
else:
    if (turno == "diurno"):
        pagamento = areiaDiurno
    else:
        pagamento = areiaNoturno

print ("sua passagem custa R$ %0.2f"%pagamento)


