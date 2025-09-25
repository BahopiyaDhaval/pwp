#Bahopiya Dhaval
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 4, 6, 8]
plt.plot(x, y1, label='y = x²')
plt.plot(x, y2, label='y = 2x')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Multiple Lines Plot')
plt.legend()
plt.show()