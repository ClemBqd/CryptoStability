from model import BtcModel
import matplotlib.pyplot as plt
import pandas

import matplotlib.pyplot as plt 
from pandas import DataFrame


empty_model = BtcModel(100)
#print(empty_model.kapital_households)

for i in range(2):
    empty_model.step()

#agent_kapital = [a.kapital for a in empty_model.schedule.agents]
agent_wage = [a.wage for a in empty_model.schedule.agents]
#test1 = empty_model.bank.deposits

#print(agent_kapital)
#print(agent_wage)
#print(empty_model.kapital_households)
#print(empty_model.kapital_households_speculators)

gini = empty_model.datacollector.get_model_vars_dataframe()
print(gini)
# gini.plot()
# plt.show()

agent_wages = empty_model.datacollector.get_agent_vars_dataframe()
agent_wages.head()
print(agent_wages)

#one_agent_wage = agent_wages.xs(14, level="AgentID")
#one_agent_wage.Wage.plot()


#end_wealth = agent_wages.xs(level="Step")["Wage"]
#end_wealth.hist(bins=range(agent_wages.Wages.max()+1))

# print(test1)
# plt.hist(agent_kapital)
#plt.show()
