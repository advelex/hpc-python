import numpy as np

flat = np.arange(16, dtype=float)
matrix = flat.reshape((4, 4))
print(matrix)

print('\nSecond row')
print(matrix[1, :])

print('\nThrid column')
print(matrix[:, 2])

print('\nPartial assignment')
matrix[:2, :2] = 0.21
print(matrix)


row1 = np.zeros(8)
row1[::2] = np.ones(8)[::2]
row2 = np.ones(8)
row2[::2] = np.zeros(8)[::2]
result = np.array([globals()[f'row{(i%2)+1}'] for i in range(8)])
print(result)
