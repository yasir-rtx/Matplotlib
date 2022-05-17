import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls") 

sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))
plt.plot(sudut,y)
plt.ylabel('magnituda')
plt.xlabel('sudut')

# Mengganti ticks
plt.xticks(
    [0,90,180,270,360],
    [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$',]
    )
plt.yticks([-1,0,1])

plt.show()