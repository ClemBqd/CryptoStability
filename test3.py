from model import BtcModel
import matplotlib.pyplot as plt
import pandas


import matplotlib.pyplot as plt 
from pandas import DataFrame

empty_model = BtcModel(10)

for i in range(20):
    empty_model.step()

households_kapital = [a.kapital for a in empty_model.schedule.agents]
print(households_kapital)
