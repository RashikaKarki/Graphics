from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from numpy import sin, cos

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)


d = [-2, 2]
for s, e in combinations(np.array(list(product(d,d,d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        ax.plot3D(*zip(s,e), color="g")
    
sx, sy, sz = [int(x) for x in input("Enter scaling factors Sx, Sy and Sz: ").split()]

for s, e in combinations(np.array(list(product(d,d,d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        s_rotated = [s[0] * sx, 
                    s[1] * sy,
                    s[2] * sz]
        e_rotated = [e[0] * sx, 
                    e[1] * sy,
                    e[2] * sz]      
        ax.plot3D(*zip(s_rotated,e_rotated), color="r")


plt.legend(["Orginal"], loc ="lower right") 

plt.show()