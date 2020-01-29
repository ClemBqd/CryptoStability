from model import BtcModel
import matplotlib.pyplot as plt
import pandas


import matplotlib.pyplot as plt 
from pandas import DataFrame
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

empty_model = BtcModel(10)

for i in range(20):
    empty_model.step()

#households_kapital = [a.kapital for a in empty_model.schedule.agents]
#print(households_kapital)

gini = empty_model.datacollector.get_model_vars_dataframe()
print(gini)

agent_wages = empty_model.datacollector.get_agent_vars_dataframe()
print(agent_wages)