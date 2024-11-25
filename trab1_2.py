import math
from integracao_numerica import metodoDeSimpson, metodoDosTrapezios
import matplotlib.pyplot as plt

#2.

# a.

f = lambda x: math.e ** (-x**2)

x1, y1, r1 = metodoDosTrapezios(f, 0, 1, 10)
x2, y2, r2 = metodoDeSimpson(f, 0, 1, 10)

for i in range(len(x1)):
    print(f'{x1[i]:.3f}', ', ', f'{y1[i]:.3f}')

print('Resultado = ', r1)

print()

for i in range(len(x2)):
    print(f'{x2[i]:.3f}', ', ', f'{y2[i]:.3f}')
print('Resultado = ', r2)

print()

# b.

f = lambda x: math.log((x + math.sqrt(x+1)))

x1, y1, r1 =  metodoDosTrapezios(f, 1, 2, 6)
x2, y2, r2 =  metodoDeSimpson(f, 1, 2, 6)

for i in range(len(x1)):
    print(f'{x1[i]:.3f}', ', ', f'{y1[i]:.3f}')

print('Resultado = ', r1)

print()

for i in range(len(x2)):
    print(f'{x2[i]:.3f}', ', ', f'{y2[i]:.3f}')
print('Resultado = ', r2)

