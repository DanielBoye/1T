import matplotlib.pyplot as plt
from pylab import *

"""
Energi = J
Effekt = W
Intensitet = W/m^2 (m = meter)
"""

r = 1
effekt = 100
avstand_max = 15

liste_r = []
liste_intensitet = []

def E(r):
    intensitet = effekt * (1 / (r*r))
    return intensitet

while r <= avstand_max:
    liste_r.append(r)
    liste_intensitet.append(E(r))
    r += 0.1

plt.plot
plt.xlabel("")
plt.ylabel("Intensitet")
plt.show()
