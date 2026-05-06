import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read data from .csv file
data = pd.read_csv('2.4.1 .csv')

# Extract x and y data from the dataframe
h1 = data['h1']
t1 = (data['t1'] + 273.15)
h2 = data['h2']
t2 = (data['t2'] + 273.15)

y1 = np.log(h1)
x1 = 1 / t1
y2 = np.log(h2)
x2 = 1 / t2

# Plot data with error bars
plt.errorbar(x1*10**3, y1, xerr=0.05/(t1**2), yerr=0.04/h1, fmt='o', capsize=5, color='blue', markersize= 0, ecolor="black")
plt.scatter(x1*10**3, y1, color='blue', s= 10, label= 'Нагрев')

plt.errorbar(x2*10**3, y2, xerr=0.05/(t1**2), yerr=0.04/h1, fmt='o', capsize=5, color='red', markersize= 0, ecolor="black",)
plt.scatter(x2*10**3, y2, color='red', s= 10, label = 'Остывание', marker='v')

plt.xlim([3.18, 3.42])
plt.ylim([0.4, 1.7])



plt.xlabel('$1/T, K^{-1} \cdot 10^{-3}$')
plt.ylabel('$ln(H)$')
plt.title('Зависимость $ln(H)$ от $1/T$')
plt.grid(True)
plt.legend(fontsize=12)
plt.show()