import mpl_toolkits.mplot3d as pt3d
import matplotlib.pyplot as pt
import numpy as np

height = np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 185, 145, 168, 172, 181, 169])
weight = np.array([86, 74, 66, 78, 68, 79, 90, 73, 70, 88, 66, 84, 67, 84, 77])
axes = pt.axes(projection="3d")
# axes.plot3D(height, weight)
axes.scatter3D(height,weight)
axes.set_xlabel("Height")
axes.set_ylabel("Weight")
pt.show()
