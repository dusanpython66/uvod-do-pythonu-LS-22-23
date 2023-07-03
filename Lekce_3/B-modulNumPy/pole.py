# importujme modul numpy
import numpy as np

# při volání z modulu numpy použijeme zkratku np

# vytvořme pole
vektor1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# vytvořme pole
vektor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# sčítání vektorů: vektor1 + vektor2
print(vektor1 + vektor2)

# skalární násobení vektoru: vektor1 * 2

# skalární součin dvou vektorů: vektor1 * vektor2
soucin = np.dot(vektor1, vektor2)
print(soucin)

# Vytvořme matice
matice1 = np.array([[1, 2, 0], [4, 5, 6], [7, 8, 9]])
print(matice1)

# Spočítejme determinant matice
determinant = np.linalg.det(matice1)
print(determinant)

# Určeme inverzní matici
inverzni_matice = np.linalg.inv(matice1)
print(inverzni_matice)


