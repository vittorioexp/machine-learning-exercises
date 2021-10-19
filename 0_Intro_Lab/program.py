#%%

#import all required packages
import matplotlib.pyplot as plt
import csv
from scipy import stats
import numpy as np
import sklearn as sl
from sklearn import linear_model


filename = "0_intro_Lab/data/km_year_power_price.csv"

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)

print(headers)
print(data.shape)
print(data[:3])


stats.linregress()

sl.linear_model.LinearRegression() # note: it requires fit() method

slope, intercept, r_value, p_value, std_err = stats.linregress(data[:,1], data[:,3])


plt.plot(data[:,1], data[:,3], 'o', label='original data')
plt.plot(data[:,1], intercept + slope*data[:,1], 'r*', label='fitted line linregress')
plt.plot(data[:,1], float(reg.intercept_) + float(reg.coef_)*data[:,1], 'y+', label='fitted line Linear Model')
plt.plot(data[:,1], w[0] + w[1]*data[:,1], 'g', label='fitted line Least Squares')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Price [$]')
plt.show()