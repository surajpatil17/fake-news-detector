import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = np.arange(5, 20)
y = np.exp(x/3)
f = interp1d(x, y)

x1 = np.arange(6, 12)
plt.plot(x, y, 'o', x1, f(x1), '--')
plt.show()
