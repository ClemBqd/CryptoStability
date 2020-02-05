from model import BtcModel, SinuModel, P0, P1, P2
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from model import BtcModel
import pandas
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt 

btc_model = BtcModel(20, 'pfebtc.xlsx')

for i in range(36):
    btc_model.step()
'''
# Test SinuModel avec variation réelle du bitcoin
sinu_model = SinuModel(20,'pfebtc.xlsx', btc_model.kapital_global_btcModel)
for i in range(36):
    sinu_model.step()

rate = sinu_model.sinu_datacollector.get_model_vars_dataframe()
#print(rate)
plt.subplot(211)
plt.plot(rate)

# Test SinuModel avec variation "stable" du bitcoin
sinu_model_stable = SinuModel(20,'pfestable.xlsx', btc_model.kapital_global_btcModel)
for i in range(36):
    sinu_model_stable.step()

rate2 = sinu_model_stable.sinu_datacollector.get_model_vars_dataframe()
#print(rate2)
plt.subplot(212)
plt.plot(rate2)
plt.show()

# Test avec modularServer 
'''
kapital_households_chart = ChartModule([{"Label" : "KapitalH",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 
rate_chart = ChartModule([{"Label" : "Rate",
                            "Color": "Black"}],
                            data_collector_name="sinu_datacollector")

kapital_households_global_chart = ChartModule([{"Label" : "KapitalG",
                                                "Color": "Red"}],
                                                data_collector_name="datacollector") 


server2 = ModularServer(SinuModel,
                        [kapital_households_chart, kapital_households_global_chart, rate_chart],
                        "SinuModel",
                        {"n_households":20, "df3": 'pfebtc.xlsx', "list_kapital_global": btc_model.kapital_global_btcModel})

server2.port = 8524 #The default
server2.launch()

