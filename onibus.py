# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18bMhKtzW2pc5VcVq56pivCK03N_9PtkF
"""

qtpessoas = int (input("quantas pessoas vão viajar? " ))
onibuspipa = float (input("quanto custa o aluguel do onibus para Pipa? "))
onibusporto = float (input("quanto custa o aluguel do onibus para Porto de Galinhas? "))
if onibuspipa < onibusporto:
    x = onibuspipa/qtpessoas
    print ("o aluguel do ônibus para Pipa é mais barato, e custará %.2f"%x, " reais para cada pessoa" )
if onibusporto < onibuspipa:
    y = onibusporto/qtpessoas
    print ("o aluguel do ônibus para Porto de Galinhas é mais barato, e custará %.2f"% y, " reais para cada pessoa")