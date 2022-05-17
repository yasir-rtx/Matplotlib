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
t3,y3 = sinusGenerator(1,1,4,180)

data1 = plt.plot(t1,y1)
data2 = plt.plot(t2,y2)
data3 = plt.plot(t3,y3)

# Set properties
# plt.setp(plotName, properti='nilai')
plt.setp(data1, color='r', linestyle='dotted')
plt.setp(data2, color='g', linewidth=4)
plt.setp(data3, color='b')

plt.show()