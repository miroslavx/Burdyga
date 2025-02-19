import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
x1 = np.linspace(-12, 12, 200)
y1 = -1/18 * x1**2 + 12
x2 = np.linspace(-4, 4, 100)
y2 = -1/8 * x2**2 + 6
x3 = np.linspace(-12, -4, 100)
y3 = -1/8 * (x3 + 8)**2 + 6
x4 = np.linspace(4, 12, 100)
y4 = -1/8 * (x4 - 8)**2 + 6
x5 = np.linspace(-4, -0.3, 100)
y5 = 2*(x5 + 3)**2 - 9
x6 = np.linspace(-4, 0.2, 100)
y6 = 1.5*(x6 + 3)**2 - 10

plt.plot(x1, y1, 'b.-', markersize=2)  
plt.plot(x2, y2, 'c.-', markersize=2) 
plt.plot(x3, y3, 'm.-', markersize=2) 
plt.plot(x4, y4, 'y.-', markersize=2)  
plt.plot(x5, y5, 'g.-', markersize=2)  
plt.plot(x6, y6, 'r.-', markersize=2)  
plt.grid(True)
plt.title('Vihmavari')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-12, 12, -10, 12])
plt.show()