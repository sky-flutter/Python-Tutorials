import numpy as np
import matplotlib.pyplot as pt

data = np.random.randn(1000)
pt.title("Histogram Title")
pt.xlabel("Random Data")
pt.ylabel("Frequency")
pt.hist(data, 10)
pt.show()
