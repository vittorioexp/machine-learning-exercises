#%%

# Linear Regression using sklearn.linear_model.LinearRegression

import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn.linear_model import LinearRegression


filename = "data/km_year_power_price.csv"

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)

x = data[:,1].reshape((-1, 1))
y = data[:,3]

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)
print('slope:', model.coef_)


plt.plot(x, y, 'o', label='original data')
plt.plot(x, model.intercept_ + model.coef_*x, 'r*', label='fitted line linregress')
#plt.plot(x, float(reg.intercept_) + float(reg.coef_)*x, 'y+', label='fitted line Linear Model')
#plt.plot(data[:,1], w[0] + w[1]*data[:,1], 'g', label='fitted line Least Squares')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Price [$]')
plt.show()