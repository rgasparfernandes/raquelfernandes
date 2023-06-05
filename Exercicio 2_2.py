# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:59:46 2023

@author: Raquel Fernandes
"""

numero = int(input("Indique um número inteiro: "))
if numero %2 == 0:
    mensagem = "numero par"
else:
    mensagem = "numero impar"
    
print(mensagem)