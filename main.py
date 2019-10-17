import numpy as np
import matplotlib.pyplot as pt

x = np.arange(1, 5)
y = x ** 3

pt.figure(figsize=(5, 5))
pt.plot([1, 2, 3, 4], [1, 4, 9, 16], "go", x, y, 'r^')
# pt.plot([1, 2, 3, 4], [1, 4, 9, 16], "go")
pt.title("Sample Graph Plot")
pt.xlabel('X Label')
pt.ylabel('Y Label')
pt.show()
