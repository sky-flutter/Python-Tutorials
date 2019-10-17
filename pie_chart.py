import matplotlib.pyplot as pt
import numpy as np

firms = ["Firm A", "Firm B", "Firm C", "Firm D", "Firm E"]
market_share = [20, 25, 10, 20, 50]
Explode = [0, 0, 0, 0, 0]

pt.pie(market_share, explode=Explode, labels=firms, shadow=False, startangle=45,
       colors=["green", "blue", "red", "yellow", "pink"])
pt.axis('equal')
pt.legend(title="Firms")
pt.show()
