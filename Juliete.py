# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zanczLz7UEomA0iTZtQ2TUjz_6dZVBYQ
"""

novoSalario = float(input ("qual o valor de seu novo salario "))

if (novoSalario < 2000):
    print ("você poderá conhecer a Argentina!")
elif (novoSalario >= 2000) and (novoSalario <= 3000):
    print ("você poderá conhecer a Espanha!")
elif (novoSalario > 3000):
    print ("você poderá conhecer a Alemanha!")