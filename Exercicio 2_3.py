# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:09:21 2023

@author: Raquel Fernandes
"""

lista = []

numeros = input("indique 5 números inteiros separados por um espaço:")

lista = [int(numero) for numero in numeros.split()]

print("Números pares são: ")

for numero in lista:
        if numero %2 == 0:
            print (numero)