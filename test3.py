from model import BtcModel
import matplotlib.pyplot as plt
import pandas
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

import matplotlib.pyplot as plt 
from pandas import DataFrame
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

empty_model = BtcModel(10, 'pfebtc.xlsx')
'''
print(empty_model.sum_loans_households)
print("KapitalG: ",empty_model.kapital_global)
households_loan = [a.loan for a in empty_model.schedule.agents]
print(households_loan)
print(sum(households_loan))
print("--------------------------")
'''

print(empty_model.current_datetime)
for i in range(5):
    empty_model.step()
    households_kapital = [a.kapital for a in empty_model.schedule.agents]
    print("Sum Households", sum(households_kapital))
    print(empty_model.kapital_global)
    x = sum(households_kapital) - empty_model.kapital_global
    print("Diff: ", x)
    print(households_kapital)
    print("--------------------------") 

'''
households_conso = [a.conso for a in empty_model.schedule.agents]
print("Sum conso: ", sum(households_conso))
print("Empty model sum_consumption :", empty_model.sum_consumption_households)
#gini = empty_model.datacollector.get_model_vars_dataframe()
#print(gini)
#gini=empty_model.datacollector.model_vars["Production"][-1]
#print(gini)
print("Kapital Global: ", empty_model.kapital_global)
gini=empty_model.datacollector.model_vars["KapitalG"][-1]
print(gini)
print("--------------------------")
print(empty_model.kapital_global)
print(empty_model.kh)
print(empty_model.kh_high)
print(empty_model.kh_medium)
print(empty_model.kh_low)
'''