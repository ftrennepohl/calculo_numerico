import math
from sistemas_lineares import metodoDeGauss
import matplotlib.pyplot as plt

# Função para resolver usando diferenças finitas
def problemaDoValorDeContorno(h, x_start=0, x_end=1, y_start=0, y_end=math.e):
    # Número de pontos
    n = int((x_end - x_start) / h) + 1
    x = [x_start + i * h for i in range(n)]
    
    # Sistema linear: matriz e vetor
    A = [[0 for _ in range(n)] for _ in range(n)]
    b = [0 for _ in range(n)]
    
    # Preenchendo as condições de contorno
    A[0][0] = 1  # y(0) = y_start
    b[0] = y_start
    A[-1][-1] = 1  # y(1) = y_end
    b[-1] = y_end
    
    # Preenchendo o sistema linear com diferenças finitas
    for i in range(1, n-1):
        xi = x[i]
        A[i][i-1] = 1 / h**2 - 1 / (2 * h)
        A[i][i] = -2 / h**2 - xi
        A[i][i+1] = 1 / h**2 + 1 / (2 * h)
        b[i] = -math.exp(xi) * (xi**2 + 1)

    mat = A.copy()
    for i in range(n):
        mat[i].append(b[i])

    return x, metodoDeGauss(mat)

hs = [0.1, 0.05, 0.01]
solutions = [problemaDoValorDeContorno(h) for h in hs]
xs = [solution[0] for solution in solutions]
ys = [solution[1] for solution in solutions]


plt.figure(figsize=(10, 6))
for i, (x, y) in enumerate(solutions):
    plt.plot(x, y, label=f"h = {hs[i]}")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Soluções Aproximadas para Diferentes Valores de h")
plt.legend()
plt.grid(True)
plt.show()
