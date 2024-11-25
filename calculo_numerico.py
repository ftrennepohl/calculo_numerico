import math

'''
Raízes de funções:

Método da bissecção
Método da posição falsa
Método das cordas
Método de Newton
Método da Secante
'''

def metodoBissecao(f, a, b, epsilon):
    if(f(a) * f(b) > 0): print("Não existe raiz dentro do intervalo")
    if(b-a < epsilon): return (a + b) / 2
    ai = a
    bi = b
    while(bi-ai > epsilon):
        xi = (bi+ai)/2
        if f(xi) * f(ai) > 0:
            ai = xi
        else:
            bi = xi
    return (ai + bi) / 2

def metodoPosicaoFalsa(f, a, b, epsilon1, epsilon2):
    if(f(a) * f(b) > 0): print("Não existe raiz dentro do intervalo")
    if(b-a < epsilon1): return (a + b) / 2
    if(abs(f(a)) < epsilon2): return a
    if(abs(f(b)) < epsilon2): return b
    ai = a
    bi = b
    xi = (a * f(b) - b * f(a)) / (f(b) - f(a))
    while(b-a > epsilon1):
        xi = (ai * f(bi) - bi * f(ai)) / (f(bi) - f(ai))
        if(abs(f(xi)) < epsilon2): return xi
        if f(xi) * f(ai) > 0:
            ai = xi
        else:
            bi = xi
    return ai, bi

def metodoDasCordas(f, f_dx2, a, b, epsilon1, epsilon2):
    if(f(a) * f(b) > 0): print("Não existe raiz dentro do intervalo")
    if(b-a < epsilon1): return (a + b) / 2
    if(abs(f(a)) < epsilon2): return a
    if(abs(f(b)) < epsilon2): return b
    # aproximação incial
    x0 = (a + b) / 2
    if(f(a) * f_dx2(x0) > 0):
        c = a
    else:
        c = b
    xi = x0 - (f(x0) / (f(x0) - f(c))) * (x0 - c)
    # iterações
    while(b-a > epsilon1):
        xi = xi - (f(xi) / (f(xi) - f(c))) * (xi - c)
        if(abs(f(xi)) < epsilon2): return xi

def metodoDeNewton(f, f_dx, x0, epsilon1, epsilon2):
    if(f(x0) < epsilon1): return x0
    xi = x0
    while(True):
        xj = xi - (f(xi) / f_dx(xi))
        if (abs(f(xj)) < epsilon1 or abs(xj - xi) < epsilon2):
            break
        xi = xj
    return xi

def metodoDaSecante(f, x0, x1, epsilon1, epsilon2):
    if(f(x0) < epsilon1): return x0
    if(f(x1) < epsilon2 or abs(x1 - x0) < epsilon2): return x1
    xi = x0
    xj = x1
    while(True):
        xk = (xi * f(xj) - xj * f(xi)) / (f(xj) - f(xi))
        if (abs(f(xk)) < epsilon1 or abs(xk - xj) < epsilon2):
            break
        xi = xj
        xj = xk
    return xk

f = lambda x : x ** 3 + 3 * x - 5
f_dx = lambda x: 3 * (x**2) + 3
f_dx2 = lambda x: x * 6

'''
print('Método bissecção: ', metodoBissecao(f, -1, 3, 0.001))
print('Método da posição falsa: ', metodoPosicaoFalsa(f, -1, 3, 0.001, 0.001))
print('Método das cordas: ', metodoDasCordas(f, f_dx2, -1, 3, 0.001, 0.001))
print('Método de Newton', metodoDeNewton(f, f_dx, 2, 0.001, 0.001))
print('Método da secante: ', metodoDaSecante(f, 2, 3, 0.001, 0.001))
'''

'''
Sistemas lineares:
- Métodos diretos: Gauss, Jordan
- Métodos iterativos: Gauss-Jacobi, Gauss-Seidel
'''

def metodoDeGauss(mat):
    n = len(mat)
    # extrair a e b
    a = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(mat[i][j])
        a.append(aux)
    b = []
    for i in range(n):
        b.append(mat[i][n])
    # eliminação
    n = len(a)-1
    for k in range(0, n):
        for i in range(k+1, n+1):
            m = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range(k+1, n+1):
                a[i][j] = a[i][j] - (m * a[k][j])
            b[i] = b[i] - (m * b[k])
    # resolução
    x = [0] * (n+1)
    x[n] = b[n] / a[n][n]
    for k in range(n-1, -1, -1):
        s = 0
        for j in range(k+1, n+1):
            s += (a[k][j] * x[j])
        x[k] = (b[k] - s) / a[k][k]
    return x


def metodoDeGaussJordan(mat):
    n = len(mat)
    # extrair a e b
    a = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(mat[i][j])
        a.append(aux)
    b = []
    for i in range(n):
        b.append(mat[i][n])
    # eliminação
    n = len(a)-1
    for k in range(0, n+1):
        for i in range(0, n+1):
            if(k != i):
                m = a[i][k] / a[k][k]
                a[i][k] = 0
                for j in range(k+1, n+1):
                    a[i][j] = a[i][j] - (m * a[k][j])
                b[i] = b[i] - (m * b[k])
    x = []
    # resolução
    for k in range(n+1):
        x.append(b[k] / a[k][k])
    return x

def testeParadaSistemasLineares(x0, x1, epsilon):
    d = []
    for i in range(len(x0)):
        d.append(abs(x1[i]-x0[i]))
    dk = max(d)
    return ((dk / abs(max(x1))) < epsilon)

def metodoDeGaussJacobi(mat, x, epsilon):
    n = len(mat)
    x0 = x.copy()
    x1 = x.copy()
    while(True):
        for i in range(n):
            bn = mat[i][n]
            for j in range(n):
                if(i != j):
                    bn -= x0[j] * mat[i][j]
            x1[i] = bn / mat[i][i]
        if(testeParadaSistemasLineares(x0, x1, epsilon)): break
        x0 = x1.copy()
    return x1

def metodoDeGaussSeidel(mat, x, epsilon):
    n = len(mat)
    x0 = x.copy()
    x1 = x.copy()
    while(True):
        for i in range(n):
            bn = mat[i][n]
            for j in range(n):
                if(i != j):
                    bn -= x1[j] * mat[i][j]
            x1[i] = bn / mat[i][i]
        if(testeParadaSistemasLineares(x0, x1, epsilon)): break
        x0 = x1.copy()
    return x1

mat = [
        [10, 2, 1, 7],
        [1, 5, 1, -8],
        [2, 3, 10, 6]
    ]

'''
print('Método de Gauss', metodoDeGauss(mat))
print('Método de Gauss-Jordan', metodoDeGaussJordan(mat))
print('Método de Gauss-Jacobi', metodoDeGaussJacobi(mat, [0.7, -1.6, 0.6], 0.001))
print('Método de Gauss-Seidel', metodoDeGaussJacobi(mat, [0.7, -1.6, 0.6], 0.001))
'''

'''
Interpolação
'''
'''
x = [-1, 0, 2]
y = [4, 1, -1]
'''

'''
x = [-1, 0, 1]
y = [4, 5, 8]
'''

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
            print(i, j)
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
    print(d)
    pn = vy[0]
    for i in range(1,n):
        pi = (d[0][i] / math.factorial(i)) * z
        for j in range(1, i):
            pi *= z - j
        pn += pi
    return pn

'''print('Interpolação linear', interpolacaoLinear(x, y))
print('Interpolação de Lagrange', interpolacaoDeLagrange(x, y, -1))  
print(interpolacaoDeGregoryNewton(x, y, 2))'''

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

y = [152, 162, 165, 170, 173, 183]'''

x = [-2, -1.5, 0, 1, 2.2, 3.1]
y = [-30.5, -20.2, -3.3, 8.9, 16.8, 21.4]



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
    return metodoDeGauss(xtx)

def ajustePolinomial(vx, vy):
    n = len(vx) # quantidade de pontos
    mx = [[x, x ** 2] for x in vx]
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
#print(ajustePolinomial(x, y))

'''
Integração numérica
'''

def metodoDosTrapezios(f, a, b, m):
    x0 = a
    xm = b
    h = (b - a) / m
    A = f(x0)
    for i in range(1, m):
        A += 2 * f(i*h)
    A += f(xm)
    A *= h/2
    return A

def metodoDeSimpson(f, a, b, m):
    x0 = a
    xm = b
    h = (b - a) / m
    A = f(x0) + f(xm)
    for i in range(1, m, 2):
        A += 4 * f(i * h)
    for i in range(2, m-1, 2):
        A += 2 * f(i * h)
    A *= h/3
    return A

'''
print(metodoDosTrapezios(lambda x: math.e ** x, 0, 1, 10))
print(metodoDeSimpson(lambda x: math.e ** x, 0, 1, 10))
'''

'''
Equações diferenciais
'''

def metodoDeEuler(f, x0, y0, h, n):
    y = y0
    for i in range(1, n):
        y = y + h * f(x0 + (i * h), y)

def metodoDeRungeKutta2(f, x0, y0, h, n):
    y = y0
    for i in range(1, n):
        xn = x0 + i * h
        # y1 = y(n+1), y0 = yn
        y = y + h/2 * (f(xn, y) + f(xn + h, y + h*f(xn, y)))
    return y

def metodoDeRungeKutta4(f, x0, y0, h, n):
    y = y0
    for i in range(1, n):
        xn = x0 + i * h
        # y1 = y(n+1), y0 = yn
        k1 = h * f(xn, y0)
        k2 = h * f(xn + h/2, y0 + k1/2)
        k3 = h * f(xn + h/2, y0 + k2/2)
        k4 = h * f(xn + h, y0 + k3)
        y = y + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

def pvi_diferencas_finitas(f, x0, y0, h, n):
    y = y0
    for i in range(n):
        xn = x0 + i * h
        
        # Diferenças finitas (avançada)
        y = y + h * f(xn, y)

    return y

def pvc_diferencas_finitas(g, a, b, ya, yb, n):

    # Discretização do intervalo
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    # Montagem do sistema linear
    A = [[0] * (n - 1) for _ in range(n - 1)]
    B = [0] * (n - 1)

    # Preenchendo a matriz A e o vetor B
    for i in range(n - 1):
        xi = x[i + 1]  # Pula o primeiro ponto (contorno)
        A[i][i] = -2 / h**2  # Diagonal principal

        if i > 0:
            A[i][i - 1] = 1 / h**2  # Elemento abaixo da diagonal
        if i < n - 2:
            A[i][i + 1] = 1 / h**2  # Elemento acima da diagonal

        B[i] = g(xi)  # Avaliação da função g no ponto xi

    # Ajuste das condições de contorno nos vetores
    B[0] -= ya / h**2
    B[-1] -= yb / h**2

    # Resolvendo o sistema linear com substituição direta (simples para este caso)
    y = [0] * (n + 1)  # Solução completa incluindo os valores de contorno
    y[0] = ya
    y[-1] = yb

    # Resolução do sistema por substituição direta (eliminando manualmente)
    for i in range(1, n):
        fator = A[i - 1][i - 1]
        for j in range(n - 1):
            A[i - 1][j] /= fator
        B[i - 1] /= fator
        for k in range(i, n - 1):
            mult = A[k][i - 1]
            for j in range(n - 1):
                A[k][j] -= mult * A[i - 1][j]
            B[k] -= mult * B[i - 1]

    # Backward substitution
    for i in range(n - 2, -1, -1):
        B[i] -= sum(A[i][j] * y[j + 1] for j in range(i + 1, n - 1))
        y[i + 1] = B[i]

    # Retorna os valores x e y aproximados
    return list(zip(x, y))