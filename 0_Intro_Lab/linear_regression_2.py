#%%

# Linear Regression using use scipy linregress function

import matplotlib.pyplot as plt
import csv
from scipy import stats
import numpy as np

filename = "data/km_year_power_price.csv"

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)

# 1 -> km
# 2 -> year
# 3 -> power
# 4 -> price

x = data[:,1]
y = data[:,3]

res = stats.linregress(x, y)

print(f"R-squared: {res.rvalue**2:.6f}")

plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line linregress')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Price [$]')
plt.show()