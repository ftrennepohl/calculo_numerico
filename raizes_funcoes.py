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


print('Método bissecção: ', metodoBissecao(f, -1, 3, 0.001))
print('Método da posição falsa: ', metodoPosicaoFalsa(f, -1, 3, 0.001, 0.001))
print('Método das cordas: ', metodoDasCordas(f, f_dx2, -1, 3, 0.001, 0.001))
print('Método de Newton', metodoDeNewton(f, f_dx, 2, 0.001, 0.001))
print('Método da secante: ', metodoDaSecante(f, 2, 3, 0.001, 0.001))
