import math
'''
Interpolação
'''


x = [-1, 0, 2]
y = [4, 1, -1]


def interpolacaoDeLagrange(vx, vy, x):
    n = len(vx)
    pn = 0
    for k in range(n):
        lk = 1
        for i in range(n):
            if i != k:
                lk *= (x - vx[i]) / (vx[k] - vx[i])
        pn += lk * vy[k]
    return pn


def interpolacaoDeNewton(vx, vy, x):
    n = len(vx)
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][0] = vy[i]
    c = n-1
    for j in range(1, n):
        for i in range(0, c):
            d[i][j] = (d[i+1][j-1] - d[i][j-1]) / (vx[i+j] - vx[i])
        c-=1
    pn = vy[0]
    for k in range(1, n):
        pk = d[0][k]
        for j in range(0, k):
            pk *= (x - vx[j])
        pn += pk
    return pn

def interpolacaoDeGregoryNewton(vx, vy, x):
    h = vx[1] - vx[0]
    z = x - vx[0]
    n = len(vx)
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][0] = vy[i]
    c = n-1
    for j in range(1, n):
        for i in range(0, c):
            d[i][j] = d[i+1][j-1] - d[i][j-1]
        c-=1
    pn = vy[0]
    for i in range(1,n):
        pi = (d[0][i] / math.factorial(i)) * z
        for j in range(1, i):
            pi *= z - j
        pn += pi
    return pn

print('Interpolação de Lagrange', interpolacaoDeLagrange(x, y, 1))  
print('Interpolação de Newton', interpolacaoDeNewton(x, y, 1))  
print('Interpolacao de Gregory-Newton', interpolacaoDeGregoryNewton(x, y, 1))