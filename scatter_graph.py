import matplotlib.pyplot as pt
import numpy as np

height = np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 185, 145, 168, 172, 181, 169])
weight = np.array([86, 74, 66, 78, 68, 79, 90, 73, 70, 88, 66, 84, 67, 84, 77])
pt.xlim(140, 200)
pt.ylim(60, 100)
pt.scatter(height, weight)
pt.title("Scatter Plot")
pt.xlabel("Height")
pt.ylabel("Weight")
pt.show()
