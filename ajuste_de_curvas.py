import math
from sistemas_lineares import *

'''
Ajuste de curvas:

Método de Mínimos Quadrados,
Ajuste Linear Múltiplo,
Ajuste polinomial
'''

#x = [1, 2, 3, 4, 5, 6, 7]
#y = [0.5, 2.5, 2.0, 4.0, 3.5, 6, 5.5]

'''mx = [
    [155, 165],
    [155, 160],
    [170, 173],
    [163, 183],
    [168, 183],
    [165, 183],
]

y = [152, 162, 165, 170, 173, 183]
'''

'''
x = [-2, -1.5, 0, 1, 2.2, 3.1]
y = [-30.5, -20.2, -3.3, 8.9, 16.8, 21.4]
'''

'''
y = [1, 2, 3, 4, 3, 4, 5, 3, 5, 5, 4, 5, 4, 5, 4, 5, 6, 0, 6, 3, 1, 3, 1]
x = [
    [0, 4, 4],
    [2, 1, 1],
    [4, 2, 2],
    [1, 3, 5],
    [5, 4, 6],
    [4, 5, 7],
    [5, 6, 8],
    [9, 7, 9],
    [9, 5, 7],
    [9, 8, 8],
    [3, 7, 7],
    [7, 8, 8],
    [8, 7, 7],
    [8, 8, 4],
    [6, 7, 3],
    [6, 8, 1],
    [5, 6, 2],
    [5, 8, 3],
    [5, 9, 4],
    [6, 2, 1],
    [6, 1, 3],
    [5, 5, 9],
    [5, 6, 7],
]'''



def metodoDeMinimosQuadrados(vx, vy):
    n = len(vx)
    # numerador b1
    b1 = n
    soma_vx = sum(vx, -vx[0])
    soma_vy = sum(vy, -vy[0])
    aux = 0
    for i in range(1, n):
        aux += vx[i] * vy[i]
    b1 *= aux
    b1 -= soma_vx * soma_vy
    # denominador b1
    denominador = n
    aux = 0
    for i in range(1, n):
        aux += vx[i] ** 2
    denominador *= aux
    denominador -= soma_vx ** 2
    b1 /= denominador
    #
    # numerador b0
    b0 = (soma_vy - b1 * soma_vx) / n
    return b0, b1

def ajusteLinearMultiplo(mx, vy):
    n = len(mx) # quantidade de pontos
    for i in range(n):
        mx[i].insert(0, 1)
    p = len(mx[0]) # quantidade de variaveis dependentes
    xt = [[0 for i in range(n)] for j in range(p)]
    for i in range(n):
        for j in range(p):
            xt[j][i] = mx[i][j]
    #
    # xtx
    xtx = [[0 for i in range(p)] for j in range(p)]
    for i in range(p):
        for j in range(p):
            xtx[i][j] = sum((xt[i][k] * mx[k][j]) for k in range(n))
    #
    # xty
    xty = [0 for i in range(p)]
    for i in range(p):
        xty[i] = sum(xt[i][j] * vy[j] for j in range(n))
    #
    # adicionar y
    for i in range(p):
        xtx[i].append(xty[i])
    for linha in xtx:
        print(linha)
    return metodoDeGauss(xtx)

def ajustePolinomial(vx, vy, grau):
    n = len(vx) # quantidade de pontos
    mx = [[x ** i for i in range(1, grau+1)] for x in vx]
    for i in range(n):
        mx[i].insert(0, 1)
    p = len(mx[0]) # quantidade de variaveis dependentes
    xt = [[0 for i in range(n)] for j in range(p)]
    for i in range(n):
        for j in range(p):
            xt[j][i] = mx[i][j]
    #
    # xtx
    xtx = [[0 for i in range(p)] for j in range(p)]
    for i in range(p):
        for j in range(p):
            xtx[i][j] = sum((xt[i][k] * mx[k][j]) for k in range(n))
    #
    # xty
    xty = [0 for i in range(p)]
    for i in range(p):
        xty[i] = sum(xt[i][j] * vy[j] for j in range(n))
    #
    # adicionar y
    for i in range(p):
        xtx[i].append(xty[i])
    return metodoDeGauss(xtx)
    
#print(metodoDeMinimosQuadrados(x, y))
#print(ajusteLinearMultiplo(x, y))