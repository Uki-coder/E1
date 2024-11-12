import numpy as np
import matplotlib.pyplot as plt


import read_file
from matplotlib import cm

def makeplot(position,angle):
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    surf = ax.plot_surface(y, x, phi, cmap = cm.hsv)
    fig.colorbar(surf, shrink=0.5, aspect=5, label=r'rozkład $\varphi$ w obszarze $XY$')
    ax.set_xlabel(r'$Y$')
    ax.set_ylabel(r'$X$')
    ax.set_zlabel(r'$\varphi[V]$')
    ax.view_init(position, angle)
    return ax

x = read_file.read_line('x_collected.txt')
y = read_file.read_row('y_collected.txt')
phi = read_file.read_matrix('phi_collected.txt')
e_min = np.gradient(phi, y, x)
e_x = -e_min[1]
e_y = -e_min[0]
x,y = np.meshgrid(x,y)
plus_electrode = plt.Circle((5, 8.5), 3.75, color='r', fill=False)


plt.rcParams['text.usetex'] = True

fig, ax = plt.subplots()

ax.add_patch(plus_electrode)
fig.set_size_inches(26,9)
x_min, y_min = [26,26],[4.5,11.5]
plt.axvline(26.5,0.2,0.75,color='black', linewidth = 4) #minus electrod
plt.legend(['katoda (cylinder)', 'anoda (płyta)'])
e_plot = plt.quiver(x,y, e_x, e_y,width = 0.001, color = 'blue', headlength = 7)
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.quiverkey(e_plot, 0.925,1.05,0.2, label=r'rozkład $\overrightarrow{E}$ w obsszarze $XY$',labelpos='E')



makeplot(20,0)
makeplot(30,30)
plt.show()

