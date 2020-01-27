from model import BtcModel
import matplotlib.pyplot as plt
import pandas

import matplotlib.pyplot as plt 
from pandas import DataFrame


empty_model = BtcModel(10)
print(empty_model.production)

print(empty_model.firm.kapital)

for i in range(2):
    agent_wage = [a.wage for a in empty_model.schedule.agents]
    households_loans = [a.loan for a in empty_model.schedule.agents]
    households_kapital = [a.kapital for a in empty_model.schedule.agents]
    print("Agent wage: ", agent_wage)
    print("Sum of agent wage: ", empty_model.sum_wages_households)
    print("Sum of agent conso: ", empty_model.sum_consumption_households)
    print("Agent loans: ", households_loans)
    print("Agent kapital: ", households_kapital)
    print("Kapital's firm: ", empty_model.firm.kapital)
    print("Firm loan :", empty_model.firm.loan)
    print("Kapital's bank : ", empty_model.bank.kapital)
    print("Production :", empty_model.production)


prod = empty_model.datacollector.get_model_vars_dataframe()
print("Production:", prod)

