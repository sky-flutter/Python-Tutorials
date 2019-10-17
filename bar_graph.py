import matplotlib.pyplot as pt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
division_avg_marks = [70, 82, 73, 65, 68]
pt.bar(divisions, division_avg_marks, color="green")
pt.title("Bar Graph")
pt.xlabel("Divisions")
pt.ylabel("Marks")
pt.show()
