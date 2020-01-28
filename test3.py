from model import BtcModel
import matplotlib.pyplot as plt
import pandas


import matplotlib.pyplot as plt 
from pandas import DataFrame

empty_model = BtcModel(20)

for i in range(2):
    empty_model.step()

households_kapital = [a.kapital for a in empty_model.schedule.agents]
print(households_kapital)
