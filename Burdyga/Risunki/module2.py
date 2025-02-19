import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 9, 100)
y1 = (2/27)*x1**2 - 3
x2 = np.linspace(-10, 0, 100)
y2 = 0.04*x2**3 - 3
x3 = np.linspace(-9, -3, 100)
y3 = (2/9)*(x3+6)**2 + 1
x4 = np.linspace(-3, 9, 100)
y4 = (1/12)*(x4-3)**2 + 6
x5 = np.linspace(5, 8.3, 100)
y5 = (1/9)*(x5-5)**2 + 2
x6 = np.linspace(5, 8.5, 100)
y6 = (1/8)*(x6-7)**2 + 1.5
x7 = np.linspace(-13, -9, 100)
y7 = -0.75*(x7+11)**2 + 6
x8 = np.linspace(-15, -13, 100)
y8 = -0.5*(x8+13)**2 + 3
x9 = np.linspace(-15, -10, 100)
y9 = np.ones_like(x9)
x10 = np.linspace(3, 4, 100)
y10 = np.ones_like(x10) * 3
plt.grid(True)
plt.title('kit')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-15, 10, -3, 7])

plt.plot(x1, y1, 'b-')  
plt.plot(x2, y2, 'orange-')  
plt.plot(x3, y3, 'g-')  
plt.plot(x4, y4, 'r-') 
plt.plot(x5, y5, 'purple-')  
plt.plot(x6, y6, 'brown-') 
plt.plot(x7, y7, 'm-')  
plt.plot(x8, y8, 'gray-')  
plt.plot(x9, y9, 'y-') 
plt.plot(x10, y10, 'c-') 
plt.figure(facecolor="lightgreen")
plt.title("Vaal")
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
ax=plt.axes()
ax.set_facecolor("lightblue")
#plt.plot(x1,y1,"r:o")
colors=["c","m","y","r","g","b","w","k","k","k","k"]
for i in range(1,11):
    plt.plot(eval(f"x{i}"), eval(f"y{i}"), colors[i-1]+"-*")
plt.show()
