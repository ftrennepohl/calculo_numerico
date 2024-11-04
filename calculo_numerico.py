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

def metodoDasCordas(fun, fun_dx, a, b, x0, epsilon):
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


def metodoDaSecante(fun, a, b, x0, epsilon):
    ai = a
    bi = b
    x_ant = x0
    xi = x0
    while(True):
        prox_x = ()
        if (criterioParada(prox_x, xi, epsilon)):
            break
        x_ant = xi
        xi = prox_x
        if fun(xi) * fun(ai) > 0:
            ai = xi
        else:
            bi = xi
    if fun(ai) < 0:
        return fun(ai), fun(bi)
    else:
        return fun(bi), fun(ai)
