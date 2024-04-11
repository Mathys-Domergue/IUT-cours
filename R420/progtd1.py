import numpy as np
import matplotlib.pyplot as plt

N=10
age = np.array([31, 30, 26, 25, 21, 31, 27, 21, 25, 32 ])
salaire = np.array([40297, 39989, 38259, 35610, 35190, 37635, 37598, 33969, 37472, 38782, ])

# Afficher les premières lignes des données
print("Age:", age[:10])
print("Salaire :", salaire[:10])

# salaire = a1*age+a0 calcul de a0 et a1

moy_a=sum(age)/np.size(age)

moy_s=sum(salaire)/np.size(salaire)
print("moyenne de x", moy_a)
print("moyenne de y",moy_s)

for i in range(10):
    a1=np.sum(((age[i]-moy_a)*(salaire[i]-moy_s))/(age[i]-moy_a)**2)
        
a0= moy_s-a1*moy_a

x_values = np.array([age.min() - 1, age.max() + 1])
y_values = a0 + a1 * x_values
plt.plot(x_values, y_values, color='red', label="Estimateur")
# Tracer les points des données
plt.scatter(age, salaire)
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()
plt.title("Régression linéaire entre salaire et age")
plt.show()