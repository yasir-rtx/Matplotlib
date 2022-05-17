import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

plt.plot(t1,y1)

# setting axis max, min
# plt.axis([xmin,xmax,ymin,ymax])
plt.axis([0, 4, -2, 2])

plt.show()