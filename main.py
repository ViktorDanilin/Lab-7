# powered by Viktor Danilin 4th variant

import numpy as np
import random
import pandas as pd
from time import perf_counter
import matplotlib as mpl
import matplotlib.pyplot as plt


# 1st task

t_start = perf_counter()
array_1 = []
array_2 = []
product = []
for i in range(1000000):
    num_1 = random.randint(1, 1000000)
    num_2 = random.randint(1, 1000000)
    array_1.append(num_1)
    array_2.append(num_2)
    product.append(array_1[i] * array_2[i])
print(perf_counter() - t_start, '[c], списки питона')

t_start = perf_counter() - t_start
array_1 = np.random.randint(0, 1000000, 1000000)
array_2 = np.random.randint(0, 1000000, 1000000)
product = np.multiply(array_1, array_2)
print(perf_counter() - t_start, '[c], numpy')


# 2nd task
file = pd.read_csv('data2.csv', delimiter=',')
data = file['Hardness']
std = file['Hardness'].std()

fig = plt.figure()
gs = fig.add_gridspec(2, hspace=1)
axs = gs.subplots(sharex=True, sharey=False)

axs[0].hist(data, bins = 20)
axs[0].set_title('Hardness')
axs[0].set_xlabel('hardness value')
axs[0].set_ylabel('material number')

axs[1].hist(data,bins = 20, density=True)
axs[1].set_title('Normalized hardness')
axs[1].set_xlabel('hardness value')
axs[1].set_ylabel('material number')
for ax in axs:
    ax.label_outer()
print(round(std, 2), 'среднеквадратичное отклонение')


# 3rd task
