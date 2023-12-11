import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl.mesh import Mesh

# Load the 3D mesh from the .stl file
your_mesh = mesh.Mesh.from_file('3d_cube.stl')

# Get the vertices of the thing
vertices = your_mesh.vectors

# draw 3d in 2d heh
projected_vertices = vertices[:, :, :2]

# Calculate the dimensions of the floorplan
min_x = np.min(projected_vertices[:, :, 0])
max_x = np.max(projected_vertices[:, :, 0])
min_y = np.min(projected_vertices[:, :, 1])
max_y = np.max(projected_vertices[:, :, 1])
width = max_x - min_x
height = max_y - min_y

# Plot the floorplan
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.plot(projected_vertices[:, :, 0].T, projected_vertices[:, :, 1].T, color='black')
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('2D Floorplan')

# Add measurements to the floorplan
for i in range(len(projected_vertices)):
    for j in range(len(projected_vertices[i])):
        x = projected_vertices[i, j, 0]
        y = projected_vertices[i, j, 1]
        ax.text(x, y, f'{x:.2f}, {y:.2f}', ha='center', va='center')

plt.show()
