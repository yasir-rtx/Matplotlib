from cProfile import label
from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)

# Tipe pertama
# plt.plot(t1,y1, label='sin(0)')
# plt.plot(t2,y2, label='sin(90)')
# plt.legend()

# Tipe kedua
# plt.plot(t1,y1, label='sin(0)')
# plt.plot(t2,y2, label='sin(90)')
# plt.legend(loc='upper center')

# Tipe ketiga
plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.05))

# Tipe keempat
# plt.figure(1)
# ax = plt.subplot(111)
# plt.plot(t1,y1, label='sin(0)')
# plt.plot(t2,y2, label='sin(90)')
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width=0.7, box.height])
# plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.05))

plt.show()