#%%
from model import BtcModel
import matplotlib.pyplot as plt 

empty_model = BtcModel(3)
print(empty_model.kapital_households)

for i in range(2):
    empty_model.step()

agent_kapital = [a.kapital for a in empty_model.schedule.agents]
agent_wage = [a.wage for a in empty_model.schedule.agents]
# test1 = empty_model.bank.deposits

print(agent_kapital)
print(agent_wage)
print(empty_model.kapital_households)
# print(test1)
# plt.hist(agent_kapital)
# plt.show()
# %%
