def criterioParada(xi, xj, epsilon):
    return True if abs(xj - xi) < epsilon else False 

def metodoBissecao(fun, a, b, epsilon):
    n = 0
    ai = a
    bi = b
    while((bi-ai)/(2^n) < epsilon):
        xi = bi+ai/2
        if fun(xi) * fun(ai) > 0:
            ai = xi
        else:
            bi = xi
        n+=1
    return fun(ai), fun(bi)

def metodoPosicaoFalsa(fun, a, b, epsilon):
    ai = a
    bi = b
    xi = a * fun(b) - b * fun(a)
    while(True):
        prox_x = a * fun(b) - b * fun(a)
        if (criterioParada(prox_x, xi, epsilon)): break
        if fun(xi) * fun(ai) > 0:
            ai = xi
        else:
            bi = xi
    return fun(ai), fun(bi)

def metodoDasCordas(fun, fun_dx, a, b, epsilon):
    '''
    c = extremo a ser calculado
    d = extremo fixado
    '''
    if(fun_dx(a) * fun(a) > 0):
        c = a
    else:
        c = b
    xi = xi - (fun(xi) / (fun(xi) - fun(c))) * (xi)
    while(True):
        prox_x = xi - (fun(xi) / (fun(xi) - fun(c))) * (xi)
        if (criterioParada(prox_x, xi, epsilon)):
            break
        xi = prox_x
    return xi

def metodoDeNewton(fun, fun_dx, a, b, x0, epsilon):
    # x0: chute inicial
    ai = a
    bi = b
    xi = x0
    while(True):
        prox_x = xi / (fun(xi) / fun_dx(xi))
        if (criterioParada(prox_x, xi, epsilon)):
            break
        xi = prox_x
        if fun(xi) * fun(ai) > 0:
            ai = xi
        else:
            bi = xi
    if fun(ai) < 0:
        return fun(ai), fun(bi)
    else:
        return fun(bi), fun(ai)


def metodoDaSecante(fun, a, b, x0, x1, epsilon):
    '''
    x0, x1: chutes
    xi: xn-1
    xj: xn
    '''
    ai = a
    bi = b
    xi = x0
    xj = x1
    while(True):
        prox_x = (xi * fun(xj) - x1 * fun(xi)) / (fun(xj) - fun(xi))
        if (criterioParada(prox_x, xi, epsilon)):
            break
        xi = xj
        xj = prox_x
        if fun(xi) * fun(ai) > 0:
            ai = xi
        else:
            bi = xi
    if fun(ai) < 0:
        return fun(ai), fun(bi)
    else:
        return fun(bi), fun(ai)

'''
Sistemas lineares:
- Métodos diretos: Gauss, Jordan
- Métodos iterativos: Gauss-Jacobi, Gauss-Seidel
'''

def metodoDeGauss(a, b, x):
    # eliminação
    n = len(a)
    for k in range(1, n):
        for i in range(k, n+1):
            m = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range(k+i, n+1):
                a[i][j] = a[i][j] - m * a[k][j]
                b[i] = b[i] - m*b[k]
    # resolução
    x[n] = b[n]/a[n][n]
    for k in range(n-1, 1, -1):
        s = 0
        for j in range(k+1, n+1):
            s = s + a[k][j] * x[j]
        x[k] = (b[k] - s) / a[k][k]

