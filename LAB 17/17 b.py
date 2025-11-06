#Bahopiya Dhaval

from sympy import symbols, Sum, oo, cos

n, z, w = symbols('n z w')
x_n = cos(w * n)


X_z = Sum(x_n * z**(-n), (n, 0, oo)).doit()
closed_form_X_z = X_z.simplify() 


print("The Z-transform X(z) is:")
print(closed_form_X_z)