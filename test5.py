from model import BtcModel, SinuModel, P0, P1, P2
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from model import BtcModel
import pandas
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt 

btc_model = BtcModel(20, 'pfebtc.xlsx')
sum_households_kapital_btc = []
for i in range(36):
    btc_model.step()
    households_kapital_btc = [a.kapital for a in btc_model.schedule.agents]
    sum_households_kapital_btc.append(sum(households_kapital_btc))
    print(i)

print(sum_households_kapital_btc)
# Test SinuModel avec variation réelle du bitcoin avec sum_kapital_global
sinu_model = SinuModel(20,'pfebtc.xlsx', sum_households_kapital_btc)
for i in range(16): #in range(16) et pas (36) car index error dans la calcul de taux à partir de 17
    sinu_model.step()
    print("Test: ", i)

rate = sinu_model.sinu_datacollector.get_model_vars_dataframe()
#print(rate)
plt.subplot(211)
plt.plot(rate)

# Test SinuModel avec variation "stable" du bitcoin
sinu_model_stable = SinuModel(20,'pfestable.xlsx', sum_households_kapital_btc)
for i in range(16):
    sinu_model_stable.step()

rate2 = sinu_model_stable.sinu_datacollector.get_model_vars_dataframe()
#print(rate2)
plt.subplot(212)
plt.plot(rate2)
plt.show()
