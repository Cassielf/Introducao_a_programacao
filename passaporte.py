pais=str.lower(input("Qual o país de destino? "))
tipoPassaporte = str.lower(input ("Passaporte novo ou renovação? "))

PortugalEspanhaFranca = 120
DinamarcaNZelandia = 180
novo= 130
renovacao = (novo/2)


if (pais == "portugal") or (pais == "espanha") or (pais == "frança"):
    taxaVisto = PortugalEspanhaFranca 
elif (pais == "dinamarca") or (pais == "nova zelandia"):
    taxaVisto = DinamarcaNZelandia
    print ("Esse país exige vacina contra a febre amarela")
else:
    taxaVisto = 0


if (tipoPassaporte == "novo"):
    taxaPassaporte = novo
else:
    taxaPassaporte = renovacao

pagamento = taxaVisto+taxaPassaporte

print ("o valor a ser pago é R$ {0:.2f}".format(pagamento))
    
    
    
