from model import BtcModel, SinuModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from model import BtcModel
import pandas
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt 

empty_model = BtcModel(100, 'pfebtc.xlsx')

for i in range(20):
    empty_model.step()

kapital_households_chart = ChartModule([{"Label" : "KapitalH",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 
server2 = ModularServer(SinuModel,
                        [kapital_households_chart],
                        "SinuModel",
                        {"n_households":20, "df3": 'pfebtc.xlsx', "list_kapital_global": empty_model.kapital_global_btcModel})

server2.port = 8523 #The default
server2.launch()