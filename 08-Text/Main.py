import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

plt.plot(t,y)

# Menambah text
# plt.text(x,y,'text')
plt.text(2,0.5,r'$ y = \mathcal{A}.sin(2 \omega t) $')

plt.show()