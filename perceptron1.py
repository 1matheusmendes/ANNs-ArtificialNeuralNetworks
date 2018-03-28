# -*- coding: utf-8 -*-
"""
Spyder Editor

@autor: Matheus Mendes
Este é um arquivo de script temporário.
"""
entradas = [-1, 7, 5] #ENTRADAS "NEURÔNIO"
pesos = [0.8, 0.1, 0] #PESOS "SINAPSES"

def soma (e, p): #FUNÇÃO SOMA
    s = 0
    for i in range(3): #CORRENDO A LISTA, COM RANGE DE 3 POIS SÓ TEM 3 POSIÇÕES NO VETOR
        print(entradas[i])
        print(pesos[i])
        s += e[i] * p[i] #FUNÇÃO SOMA
    return s #RETORNA O VALOR DA SOMA        
        
s = soma(entradas, pesos) #INSTANCIA S = SOMA      

def stepFunction(soma): #FUNÇÃO DEGRAU
    if (soma >= 1): #VERIFICA O VALOR ESTABELECIDO NA FUNÇÃO DEGRAU
        return 1 #SE MAIOR QUE 1 RETORNA 1, REPRESENTA TUDO
    return 0 #CASO CONTRARIO RETORNA ZERO, REPRESENTA NADA

r = stepFunction(s) #INSTANCIA DA FUNÇÃO DEGRAU

print ("Resultado da função degrau")
print (s)

  
#teste Fetching latest commit…  