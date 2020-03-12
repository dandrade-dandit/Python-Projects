from statistics import mean
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style


a=float(input("Entre com o primeiro numero: "));
b=float(input("Entre com o segundo numero : "));
if (b!=0):
    print ("O resultado da divisao eh: " + str(a/b));
else:
    print ("Divisao por zero! Digite um numero maior que zero para os paramentros de entrada!");


xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 3, 2, 5, 7], dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs)))

    b = mean(ys) - m * mean(xs)

    return m, b


m, b = best_fit_slope_and_intercept(xs, ys)

print('m is equal to: ' + str(round(m, 2)))
print('b is equal to: ' + str(round(b, 2)))

# Calculate a line using a list comprehension
line = [(m*x)+b for x in xs]

print(line)

# Plot
style.use('ggplot')

plt.scatter(xs,ys,color='#003F72',label='Data')
plt.plot(xs, line, label='Regression Line (Historical Data)')
plt.legend(loc=4)
plt.show()

# New value to x
predict_x = 6

# Predicting the value of y
predict_y = (m*predict_x)+b
print(predict_y)

#xs = np.array([1,2,3,4,5], dtype=np.float64)
#ys = [(m*x)+b for x in xs]

# Plot
predict_x = 6
predict_y = (m * predict_x) + b

xs = np.append(xs, predict_x)
ys = np.append(ys, predict_y)

line = [(m * x) + b for x in xs]

plt.scatter(xs, ys, color='#003F72', label='Data')
plt.plot(xs, line, label='Regression Line (Prediction)')
plt.legend(loc=4)
plt.show()