'''
Sistemas lineares:
- Métodos diretos: Gauss, Jordan
- Métodos iterativos: Gauss-Jacobi, Gauss-Seidel
'''

def metodoDeGauss(mat):
    n = len(mat)  # Número de equações no sistema
    
    # Extrair matriz de coeficientes (A) e vetor de termos independentes (b)
    a = [row[:-1] for row in mat]
    b = [row[-1] for row in mat]

    # Eliminação Gaussiana
    for k in range(n):
        # Verificar pivô zero e trocar linhas, se necessário (pivotamento parcial)
        if a[k][k] == 0:
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    a[k], a[i] = a[i], a[k]
                    b[k], b[i] = b[i], b[k]
                    break
            else:
                raise ValueError("Sistema sem solução única (pivô zero detectado)")

        # Escalonamento das linhas abaixo da linha k
        for i in range(k + 1, n):
            m = a[i][k] / a[k][k]
            a[i][k] = 0  # Eliminar o elemento abaixo do pivô
            for j in range(k + 1, n):
                a[i][j] -= m * a[k][j]
            b[i] -= m * b[k]

    # Substituição retroativa para resolver o sistema
    x = [0] * n
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for k in range(n - 2, -1, -1):
        s = sum(a[k][j] * x[j] for j in range(k + 1, n))
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
