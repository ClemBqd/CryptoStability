from model import BtcModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

'''
Product = ChartModule([{"Label" : "Production",
					"Color": "Black"}],
					data_collector_name="datacollector")

server = ModularServer(BtcModel,
                    [Product],
                    "Btc Model",
                    {"n_households":10})

'''
Product = ChartModule([{"Label" : "Production",
					"Color": "Black"}],
					data_collector_name="datacollector")

kapital_households_global_chart = ChartModule([{"Label" : "KapitalG",
                                                "Color": "Black"}],
                                                data_collector_name="datacollector") 
server = ModularServer(BtcModel,
        [kapital_households_global_chart, Product],
         "Btc Model",
         {"n_households":20})

server.port = 8523 #The default
server.launch()