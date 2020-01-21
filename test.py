#%%
from model import BtcModel
import matplotlib.pyplot as plt 

empty_model = BtcModel(3)

for i in range(2):
    empty_model.step()

agent_kapital = [a.kapital for a in empty_model.schedule.agents]

print(agent_kapital)
plt.hist(agent_kapital)
plt.show()
# %%
