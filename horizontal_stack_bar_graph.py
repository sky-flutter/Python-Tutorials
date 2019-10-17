import numpy as np
import matplotlib.pyplot as pt

division = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
division_marks = [35, 40, 95, 50, 60]
boy_marks = [55, 65, 75, 85, 95]

index = np.arange(5)
width = .30

fig, ax = pt.subplots(nrows=1, ncols=1)

ax.bar(index, division_marks, width, color="green", label="Division Marks")
# ax.bar(index, boy_marks, width, color="blue", label="Boy Marks", bottom=division_marks)
ax.bar(index + width, boy_marks, width, color="blue", label="Boy Marks")

pt.title("Comparison Bar")
pt.xlabel("Divisions")
pt.ylabel("Marks")
pt.xticks(index + width / 2, division)
pt.legend(loc="best")
pt.show()
