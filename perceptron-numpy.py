# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np

entradas = np.array ([1, 7, 5]) #crinado uma array list com numpy
pesos = np.array ([0.8, 0.1, 0]) #crinado uma array list com numpy

def soma (e, p): #FUNÇÃO SOMA
    return e.dot(p) #produto escalar "soma e multiplicação das entradas"

s = soma(entradas, pesos) #INSTANCIA S = SOMA      


def stepFunction(soma): #FUNÇÃO DEGRAU
    if (soma >= 1): #VERIFICA O VALOR ESTABELECIDO NA FUNÇÃO DEGRAU
        return 1 #SE MAIOR QUE 1 RETORNA 1, REPRESENTA TUDO
    return 0 #CASO CONTRARIO RETORNA ZERO, REPRESENTA NADA

r = stepFunction(s) #INSTANCIA DA FUNÇÃO DEGRAU

print (s)