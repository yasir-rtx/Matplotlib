import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
tAkhir = 4
theta = 0
t,y = sinusGenerator(amplitudo, frekuensi, tAkhir, theta)

judul = 'Grafik Sinusoidal'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $'
parameter1 = r'$A =$' + str(amplitudo) + ' cm, '
parameter2 = r'$\omega =$' + str(frekuensi) + r'$\mathit{Hz}$'+ ' cm, '
parameter3 = r'$\theta =$' + str(theta) + r'$^{0}$'
plt.plot(t,y)

# Membuat label
plt.xlabel('waktu (detik)')
plt.ylabel('magnituda (cm)')

# Membuat judul
plt.title(judul+"\n"+rumus+"\n"+parameter1+parameter2+parameter3)

plt.show()
