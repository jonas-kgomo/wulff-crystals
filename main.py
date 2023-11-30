import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Surface energies for different crystallite orientations
energies = [1.0, 1.3, 0.8, 1.1, 1.5]  
directions = [[1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1]]

# Minimum surface energy 
gamma_min = min(energies)

# Generate coordinates of planes along each orientation
verts = []
for e,d in zip(energies,directions):
    vert = (e/gamma_min)*np.array(d)
    verts.append(vert)
    
# Generate list of faces as indices into vertex array   
faces = [[0,1,4], [1,2,4], [0,3,4], [0,2,3]] 

# Plot the Wulff shape
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for f in faces:
    ax.plot(verts[f])

ax.set_xlabel('X')
ax.set_ylabel('Y')  
ax.set_zlabel('Z')

plt.show()
