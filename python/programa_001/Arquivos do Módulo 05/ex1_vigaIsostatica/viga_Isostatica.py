import numpy as np
import math
from matplotlib import pyplot as plt

l = 5   # m
q = 10  # kN/m

x = np.linspace(0, l, 30)

Va = q * l /2
Vb = Va

momento = Va * x -(q * pow(x, 2) / 2)
cortante = Va - (q * x)

momentoMax = np.max(momento)
cortanteMax = np.max(cortante)
momentoMin = np.min(momento)
cortanteMin = np.min(cortante)

print(f'O momento máximo é: {momentoMax}')
print(f'O momento mínimo é: {momentoMin}')
print(f'O cortante máximo é: {cortanteMax}')
print(f'O cortante mínimo é: {cortanteMin}')

plt.figure(figsize=(10, 5))
plt.plot([0] * len(x), color='k')
plt.plot(-momento)
plt.plot(cortante)
plt.show()

