from mesa import Agent, Model
from mesa.time import RandomActivation
from household import Household
from bank import Bank
from firm import Firm

class BtcModel(Model):
    def __init__(self, n_households):
        self.n_households = n_households
        super().__init__()
        # Chose a schedule
        self.schedule = RandomActivation(self)
        self.production = 10
        self.kapital_households = 0
        self.kapital_households_speculators = 0

        # Create  a bank, a firm and n household
        # self.bank = Bank(1, self) 
        # self.schedule.add(bank)
        # firm = Firm(2, self)
        # self.schedule.add(firm)
    
        for i in range(self.n_households):
            h = Household(i+2, self)
            self.schedule.add(h) 

        # Create datacollector here

        # Put variable comun of all the model too

    def increase_kapital_households(self):
        for i in self.schedule.agents:
            if i.risk_profile == -1:
                self.kapital_households += i.kapital
            else:
                self.kapital_households_speculators += i.kapital




    def step(self):
        # Tell all the agents in the model to run their step function
        self.schedule.step()
        self.increase_kapital_households()
        #self.bank.step()
        # Collect data
        # self.datacollector.collect(self)

