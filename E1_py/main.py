import numpy as np
import matplotlib.pyplot as plt
import read_file
from matplotlib import cm
from matplotlib import colormaps

x = read_file.read_line('x_collected.txt')
y = read_file.read_row('y_collected.txt')
phi = read_file.read_matrix('phi_collected.txt')
e_min = np.gradient(phi, y, x)
e_x = -e_min[1]
e_y = -e_min[0]
x,y = np.meshgrid(x,y)
plus_electrode = plt.Circle((5, 8.5), 3.75, color='r', fill=False)


plt.rcParams['text.usetex'] = True
'''
fig, ax = plt.subplots()
plt.quiver(x,y, e_x, e_y)
ax.add_patch(plus_electrode)
fig.set_size_inches(26,9)
'''

plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
surf = ax.plot_surface(y, x, phi, cmap = cm.twilight_shifted)
ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_zlabel(r'\varphi')
#ax.view_init(20, 0)
ax.view_init(30,30)
plt.show()

