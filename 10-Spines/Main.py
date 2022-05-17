import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls") 

angle = np.arange(0,360,1)
y = np.sin(np.deg2rad(angle))

plt.plot(angle, y)
plt.title('Grafik Sinusoidal')
plt.text(360,0.1,'sudut')
plt.text(190,1,'magnituda')

plt.xticks(
    [0,90,180,270,360],
    [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$',]
    )
plt.yticks([-1,-0.5,0,0.5,1])

# manipulasi spines
ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()