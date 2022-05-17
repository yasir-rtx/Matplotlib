import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

"""
    1. Membuat data
    2. Membuat plot
    3. Menampilkan plot
"""

# 1.Membuat data
x = np.array([1,2,3,4,5])
y = x**2
y2 = x**2**2

# 2. Membuat plot
plt.plot(x,y)
plt.plot(x,y2)

# 3.Menampilkan plot
plt.show()