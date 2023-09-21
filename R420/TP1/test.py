import numpy as np
import matplotlib.pyplot as plt

N = 10

data_rnd = np.empty((2, N))

x = np.random.randint(low=21, high=42, size=N)
y = np.random.randint(low=35610, high=40297, size=N)

data_rnd[0] = x
data_rnd[1] = y

print(data_rnd)
