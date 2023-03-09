#Ф.И: Косарпур Киана
#ИСУ: 344494
#Вариант: 4

import numpy as np
from time import perf_counter
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter  


#Task 01

list1 = [random.random() for _ in range(1000000)]
list2 = [random.random() for _ in range(1000000)]
arr1 = np.array(list1)
arr2 = np.array(list2)

start_list = perf_counter()
list_result = [a * b for a, b in zip(list1, list2)]
end_list = perf_counter()

start_arr = perf_counter()
arr_result = np.multiply(arr1, arr2)
end_arr = perf_counter()

print("Time to perform the multiplication operation for the list:", end_list - start_list)
print("Time to perform the multiplication operation for numpy array:", end_arr - start_arr)


#Task 02

data = pd.read_csv("https://raw.githubusercontent.com/itmopython-2022/lab-7/main/data2.csv", header=None)
second_column = data[1]

plt.hist(second_column, bins=20)
plt.title("Histogram of Data2.csv (Second Column)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.hist(second_column, bins=20, density=True)
plt.title("Normalized Histogram of Data2.csv (Second Column)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()


#Task 03

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**Y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Plot of sin(x^y)')

plt.show()


#Additional task

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)


def animate(i):
    line.set_ydata(np.sin(x + i/10.0)) 
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50)

 
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  
    return line,

plt.show()

writer = PillowWriter(fps=25)  
ani.save("demo_sine.gif", writer=writer)  