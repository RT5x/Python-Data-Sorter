from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Setup
fig = plt.figure()
ax = plt.axes(projection ='3d')
plt.xlabel("x")
plt.ylabel("y")



# 3D Curve:
z = np.linspace(0, 1, 100)
x = z * np.cos(27 * z)
y = z * np.cos(27 * z)
ax.plot3D(x, y, z, 'blue')  #set color
ax.set_title('3D line plot')  # set title



#Display
plt.show()
