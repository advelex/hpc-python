import numpy as np


dx = 0.01
data = np.arange(0, np.pi/2+0.0000001, dx)
result = np.sum(np.sin((data[:-1] + data[1:])/2)*dx)
print(result)

