from model import BtcModel
import matplotlib.pyplot as plt
import pandas

import matplotlib.pyplot as plt 
from pandas import DataFrame


empty_model = BtcModel(10)
#print(empty_model.kapital_households)

print(empty_model.firm.kapital)

for i in range(2):
    empty_model.step()
    agent_wage = [a.wage for a in empty_model.schedule.agents]
    print("Agent wage: ", agent_wage)
    print("Sum of agent wage: ", empty_model.sum_wages_households)
    print("Kapital's firm: ", empty_model.firm.kapital)
    print("Kapital's bank : ", empty_model.bank.kapital)

