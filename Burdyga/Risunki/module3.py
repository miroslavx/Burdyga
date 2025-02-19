import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
x1 = np.linspace(-7, 7, 100)
y1 = 3/49 * x1**2 + 8
x2 = np.linspace(-7, 7, 100)
y2 = 49/49 * x2**2 + 1
x3 = np.linspace(-6.8, -2, 100)
y3 = -0.75*(x3 + 4)**2 + 11
x4 = np.linspace(2, 6.8, 100)
y4 = -0.75*(x4 - 4)**2 + 11
x5 = np.linspace(-5.8, -2.8, 100)
y5 = -(x5 + 4)**2 + 9
x6 = np.linspace(2.8, 5.8, 100)
y6 = -(x6 - 4)**2 + 9
x7 = np.linspace(-4, 4, 100)
y7 = 4/9 * x7**2 - 5
x8 = np.linspace(-5.2, 5.2, 100)
y8 = 4/9 * x8**2 - 9
x9 = np.linspace(-7, -2.8, 100)
y9 = -1/16 * (x9 + 3)**2 - 6
x10 = np.linspace(2.8, 7, 100)
y10 = -1/16 * (x10 - 3)**2 - 6
x11 = np.linspace(-7, 0, 100)
y11 = 1/9 * (x11 + 4)**2 - 11
x12 = np.linspace(0, 7, 100)
y12 = 1/2 * (x12 - 4)**2 - 11
x13 = np.linspace(-7, -4.5, 100)
y13 = -(x13 + 5)**2
x14 = np.linspace(4.5, 7, 100)
y14 = -(x14 - 5)**2
x15 = np.linspace(-3, 3, 100)
y15 = 2/9 * x15**2 + 2
plt.plot(x1, y1, 'b.-', markersize=2)
plt.plot(x2, y2, 'b.-', markersize=2)
plt.plot(x3, y3, 'b.-', markersize=2)
plt.plot(x4, y4, 'b.-', markersize=2)
plt.plot(x5, y5, 'b.-', markersize=2)
plt.plot(x6, y6, 'b.-', markersize=2)
plt.plot(x7, y7, 'b.-', markersize=2)
plt.plot(x8, y8, 'b.-', markersize=2)
plt.plot(x9, y9, 'b.-', markersize=2)
plt.plot(x10, y10, 'b.-', markersize=2)
plt.plot(x11, y11, 'b.-', markersize=2)
plt.plot(x12, y12, 'b.-', markersize=2)
plt.plot(x13, y13, 'r.-', markersize=2)
plt.plot(x14, y14, 'r.-', markersize=2)
plt.plot(x15, y15, 'r.-', markersize=2)
plt.grid(True)
plt.title('Kilpkonn')
plt.xlabel('x')
plt.ylabel('y')

plt.axis([-8, 8, -12, 12])

plt.show()
