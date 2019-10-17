import matplotlib.pyplot as pt
import numpy as np

x = np.arange(1, 5)
y = x ** 3

# Row wise plot
# pt.subplot(1, 2, 1)
# pt.plot([1, 2, 3, 4], [1, 4, 9, 16], "go")
# pt.title("First Plot")
#
# pt.subplot(1, 2, 2)
# pt.plot(x, y, "r^")
# pt.title("Second Plot")
#
# pt.suptitle("My Sub Plots")
# pt.show()


# Column wise plot
pt.subplot(3, 1, 1)
pt.plot([1, 2, 3, 4], [1, 4, 9, 16], "go")
pt.title("First Plot")

pt.subplot(3, 1, 2)
pt.plot(x, y, "r^")
pt.title("Second Plot")

pt.suptitle("My Sub Plots")
pt.show()
