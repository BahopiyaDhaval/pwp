#Bahopiya Dhaval

from sympy import symbols, Sum, oo

n, z = symbols('n z')
x_n = 3**n

X_z_sum = Sum(x_n * z**(-n), (n, 0, oo))
X_z = X_z_sum.doit()

print("The Z-transform X(z) is:")
print(X_z)
