import math
from integracao_numerica import *
from equacoes_diferenciais import metodoDeEuler
import matplotlib.pyplot as plt
# 3.

f = lambda x, y: y/x - (y/x) ** 2
sol_analitica = lambda x: x / (1 + math.log(x))

# a.
# soluções método de Euler

# h = 0.25
pontos_x, pontos_y = metodoDeEuler(f, 1, 1, 8, 0.25)
plt.plot(pontos_x, pontos_y, color = 'red')

erros = []
for i, x in enumerate(pontos_x):
    erros.append(abs(sol_analitica(x) - pontos_y[i]))

plt.plot(pontos_x, erros, color='red', linestyle='dashed')


# h = 0.1

pontos_x, pontos_y = metodoDeEuler(f, 1, 1, 20, 0.1)
plt.plot(pontos_x, pontos_y, color = 'green')

erros = []
for i, x in enumerate(pontos_x):
    erros.append(abs(sol_analitica(x) - pontos_y[i]))

plt.plot(pontos_x, erros, color='green', linestyle='dashed')


# h = 0.05
pontos_x, pontos_y = metodoDeEuler(f, 1, 1, 40, 0.05)
plt.plot(pontos_x, pontos_y, color = 'blue')

erros = []
for i, x in enumerate(pontos_x):
    erros.append(abs(sol_analitica(x) - pontos_y[i]))

plt.plot(pontos_x, erros, color='blue', linestyle='dashed')

#
#solução analítica
pontos_x = []
pontos_y = []

i = 1.01
while(i <= 3):
    pontos_x.append(i)
    pontos_y.append(sol_analitica(i))
    i += 0.01
plt.plot(pontos_x, pontos_y, color = 'y')

plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()