# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:27:09 2023

@author: Raquel Fernandes
"""



def calcula_area_rectangulo(comprimento , largura):
    area = comprimento * largura
    return area

comprimento = float(input("indique o comprimento: "))
largura = float(input("Indique a largura: "))

area_rectangulo = calcula_area_rectangulo(comprimento, largura)

print("A area é: ", area_rectangulo)