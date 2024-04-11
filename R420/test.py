import numpy as np
import matplotlib.pyplot as plt

N = 10
age = np.array([31, 30, 26, 25, 21, 31, 27, 21, 25, 32])
salaire = np.array([40297, 39989, 38259, 35610, 35190, 37635, 37598, 33969, 37472, 38782])

# Calculate the means
moy_a = np.mean(age)
moy_s = np.mean(salaire)

# Calculate the slope parameter
a1 = np.sum((age - moy_a) * (salaire - moy_s)) / np.sum((age - moy_a) ** 2)

# Calculate the intercept
a0 = moy_s - a1 * moy_a

# Plotting the regression line
x_values = np.array([age.min() - 1, age.max() + 1])
y_values = a0 + a1 * x_values
plt.plot(x_values, y_values, color='red', label="Estimateur")

# Plot the data points
plt.scatter(age, salaire)
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()
plt.title("Régression linéaire entre salaire et âge")
plt.show()
