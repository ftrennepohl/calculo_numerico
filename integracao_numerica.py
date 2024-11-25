import math
'''
Integração numérica
'''

def metodoDosTrapezios(f, a, b, m):
    pontos_x = []
    pontos_y = []
    x0 = a
    xm = b
    h = (b - a) / m
    A = f(x0)
    for i in range(1, m):
        xi = x0 + i*h
        A += 2 * f(xi)
        pontos_x.append(xi)
        pontos_y.append(f(xi))
    A += f(xm)
    A *= h/2
    return pontos_x, pontos_y, A

def metodoDeSimpson(f, a, b, m):
    pontos_x = []
    pontos_y = []
    x0 = a
    xm = b
    h = (b - a) / m
    A = f(x0) + f(xm)
    for i in range(1, m, 2):
        xi = x0 + i * h
        A += 4 * f(x0 + i * h)
        pontos_x.append(xi)
        pontos_y.append(f(xi))
    for i in range(2, m-1, 2):
        xi = x0 + i * h
        A += 2 * f(x0 + i * h)
        pontos_x.append(xi)
        pontos_y.append(f(xi))
    A *= h/3
    return pontos_x, pontos_y, A


'''print(metodoDosTrapezios(lambda x: (math.cos(x) + x)/math.pi, 0, 4 * math.pi, 4)[2])
print(metodoDeSimpson(lambda x: (math.cos(x) + x)/math.pi, 0, 4 * math.pi, 4)[2])'''