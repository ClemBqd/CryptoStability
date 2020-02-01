from model import BtcModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

Product = ChartModule([{"Label" : "Production",
					"Color": "Black"}],
					data_collector_name="datacollector")

kapital_households_global_chart = ChartModule([{"Label" : "KapitalG",
                                                "Color": "Red"}],
                                                data_collector_name="datacollector") 

kapital_households_chart = ChartModule([{"Label" : "KapitalH",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 

wage_households_chart = ChartModule([{"Label" : "WagesH",
                                                "Color": "Black"}],
                                                data_collector_name="datacollector") 


wage_households_sum_chart = ChartModule([{"Label" : "sum_wage",
                                                "Color": "Green"}],
                                                data_collector_name="datacollector") 

kapital_firm_chart = ChartModule([{"Label" : "KapitalF",
                                                "Color": "Red"}],
                                                data_collector_name="datacollector") 

kapital_bank_chart = ChartModule([{"Label" : "KapitalB",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 

diff1 = ChartModule([{"Label" : "diff",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 

server = ModularServer(BtcModel,
        [kapital_households_global_chart, Product, kapital_households_chart, wage_households_chart, wage_households_sum_chart, kapital_firm_chart, kapital_bank_chart,diff1],
         "Btc Model",
         {"n_households":20})

#server.port = 8523 #The default
#server.launch()