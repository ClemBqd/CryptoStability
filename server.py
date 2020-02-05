from model import BtcModel, SinuModel
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

Product = ChartModule([{"Label" : "Production",
					"Color": "Black"}],
					data_collector_name="datacollector")

kapital_households_global_chart = ChartModule([{"Label" : "KapitalG",
                                                "Color": "Red"}],
                                                data_collector_name="datacollector") 

kapital_households_chart = ChartModule([{"Label" : "KapitalH",
                                                "Color": "Red"}],
                                                data_collector_name="datacollector") 

kapital_households_risk_averse_chart = ChartModule([{"Label" : "Kapital_households_risk_averse",
                                                "Color": "Blue"}],
                                                data_collector_name="datacollector") 

kapital_households_speculator_chart = ChartModule([{"Label" : "Kapital_households_speculator",
                                                "Color": "Green"}],
                                                data_collector_name="datacollector") 


wage_households_chart = ChartModule([{"Label" : "WagesH",
                                                "Color": "Black"}],
                                                data_collector_name="datacollector") 
conso_households_chart = ChartModule([{"Label" : "Conso",
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
        [kapital_households_chart, kapital_households_global_chart ,kapital_households_risk_averse_chart, kapital_households_speculator_chart],
         "Btc Model",
         {"n_households":20, "df3": 'pfebtc.xlsx'})


#server2 = ModularServer(SinuModel,
                        #[kapital_households_global_chart],
                        #"SinuModel",
                        #{"n_households":20, "df3": 'pfebtc.xlsx', "list_kapital_global": server.kapital_global_btcModel})
#server.port = 8523 #The default
#server.launch()