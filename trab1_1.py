from ajuste_de_curvas import metodoDeMinimosQuadrados, ajustePolinomial, ajusteExponencial
import matplotlib.pyplot as plt
import math
import decimal

areas = []

with open('./area_urbana.txt', 'r', encoding="utf8") as arq:
    for line in arq:
        areas.append(line.split()[-1].replace(',', '.'))

areas = [float(area) for area in areas]


pibs = []

with open('./pib.txt', 'r', encoding="utf8") as arq:
    for line in arq:
        aux= ''
        line = line.split()
        for i in line:
            if i.isnumeric():
                aux += str(i)
        pibs.append(aux)

pibs = [int(pib) for pib in pibs]


coef = metodoDeMinimosQuadrados(areas, pibs)

# a.
plt.plot(areas, pibs, 'o')
#plt.plot([i for i in range(100)], [coef[1] * i + coef[0] for i in range(100)])

pibs2 = [math.log(pib) for pib in pibs]
coef = metodoDeMinimosQuadrados(areas, pibs2)

plt.plot([i for i in range(100)], [decimal.Decimal(math.e) ** decimal.Decimal(coef[0]) * decimal.Decimal(math.e) ** decimal.Decimal((i * coef[1])) for i in range(100)])

#c.
coef = ajustePolinomial(areas, pibs, 3)
#plt.plot([i for i in range(100)], [coef[0] + sum([coef[j] * i ** j for j in range(1, len(coef))]) for i in range(100)])


plt.xlabel("Área urbana (km^2)")
plt.ylabel("PIB municipal")

plt.show()