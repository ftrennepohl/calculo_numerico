from sistemas_lineares import metodoDeGauss

'''
Equações diferenciais
'''

def metodoDeEuler(f, x0, y0, n, h):
    pontos_x = []
    pontos_y = []
    y = y0
    for i in range(1, n+1):
        xn = x0 + i * h
        y = y + h * f(xn, y)
        pontos_x.append(xn)
        pontos_y.append(y)

    return pontos_x, pontos_y

def metodoDeRungeKutta(f, x0, y0, n, h):
    pontos_x = []
    pontos_y = []
    y = y0
    for i in range(1, n+1):
        xn = x0 + i * h
        # y1 = y(n+1), y0 = yn
        y = y + h/2 * (f(xn, y) + f(xn + h, y + h*f(xn, y)))
        pontos_x.append(xn)
        pontos_y.append(y)

    return pontos_x, pontos_y

def metodoDeRungeKutta2(f, x0, y0, n, h):
    pontos_x = []
    pontos_y = []
    y = y0
    for i in range(1, n+1):
        xn = x0 + i * h
        # y1 = y(n+1), y0 = yn
        y = y + h/2 * (f(xn, y) + f(xn + h, y + h*f(xn, y)))
        pontos_x.append(xn)
        pontos_y.append(y)

    return pontos_x, pontos_y

def metodoDeRungeKutta4(f, x0, y0, n, h):
    pontos_x = []
    pontos_y = []
    y = y0
    for i in range(1, n+1):
        xn = x0 + i * h
        # y1 = y(n+1), y0 = yn
        k1 = h * f(xn, y0)
        k2 = h * f(xn + h/2, y0 + k1/2)
        k3 = h * f(xn + h/2, y0 + k2/2)
        k4 = h * f(xn + h, y0 + k3)
        y = y + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        pontos_x.append(xn)
        pontos_y.append(y)

    return pontos_x, pontos_y

def problemaDoValorInicial(f, x0, y0, h, n):
    y = y0
    for i in range(n):
        xn = x0 + i * h
        
        # Diferenças finitas (avançada)
        y = y + h * f(xn, y)

    return y

def problemaDoValorDeContorno(f, h, x0, xn, y0, yn):
    # Número de pontos
    n = int((xn - x0) / h) + 1
    x = [x0 + i * h for i in range(n)]
    
    # Sistema linear: matriz e vetor
    A = [[0 for _ in range(n)] for _ in range(n)]
    b = [0 for _ in range(n)]
    
    # Preenchendo as condições de contorno
    A[0][0] = 1  # y(0) = y0
    b[0] = y0
    A[-1][-1] = 1  # y(1) = yn
    b[-1] = yn
    
    # Preenchendo o sistema linear com diferenças finitas
    for i in range(1, n-1):
        xi = x[i]
        A[i][i-1] = 1 / h**2 - 1 / (2 * h)
        A[i][i] = -2 / h**2 - xi
        A[i][i+1] = 1 / h**2 + 1 / (2 * h)
        b[i] = f(xi)

    mat = A.copy()
    for i in range(n):
        mat[i].append(b[i])

    return x, metodoDeGauss(mat)