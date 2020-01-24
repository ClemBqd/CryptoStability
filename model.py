from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from household import Household, loan_households
from bank import Bank
from firm import Firm

risk_lovers_rate = 0.1
#test
#test2
def increase_kapital_households(model):
       for i in model.schedule.agents:
           if i.risk_profile == -1:
               model.kapital_households += i.kapital
           else:
               model.kapital_households_speculators += i.kapital
       return model.kapital_households # A tej

class BtcModel(Model):
    def __init__(self, n_households):
        self.n_households = n_households
        super().__init__()
        # Chose a schedule
        self.schedule = RandomActivation(self)
        self.production = 10
        self.kapital_households = 0 # To change in a list of the sum 
        self.kapital_households_speculators = 0 # # To change in a list of the sum
        self.sum_loans_households = self.n_households*loan_households
        self.travail = 0
        self.alpha = 0
        self.beta = 0

        self.datacollector = DataCollector(
            model_reporters={"Kapital_household": increase_kapital_households},
            agent_reporters={"Wage": "wage"})
        # Create  a bank, a firm and n household
        # self.bank = Bank(1, self) 
        # self.schedule.add(bank)
        # firm = Firm(2, self)
        # self.schedule.add(firm)
        x = risk_lovers_rate*self.n_households
        for i in range(self.n_households):
            if i <= x:
                h = Household(i+2, 1, self)
                self.schedule.add(h)
            else:
                hp = Household(i+2, -1, self)
                self.schedule.add(hp)

        # Create datacollector here
        

        # Put variable comun of all the model too





    def step(self):
        # Tell all the agents in the model to run their step function
        self.datacollector.collect(self)
        self.schedule.step()
        increase_kapital_households(self)
        #self.bank.step()
        # Collect data
        

