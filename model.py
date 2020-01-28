from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from datetime import datetime, timedelta
from household import Household
from bank import Bank
from firm import Firm

risk_high_rate = 0.1
risk_medium_rate = 0.2
risk_low_rate = 0.2

def increase_kapital_households(model):
    kh = 0
    khp = 0
    for i in model.schedule.agents:
        if i.risk_profile == -1:
            kh += i.kapital
        else:
            khp += i.kapital    
    model.kapital_households.append(kh)
    model.kapital_households_speculators.append(khp)

def increase_wages_households(model):
    model.sum_wages_households = 0
    model.sum_consumption_households = 0
    for i in model.schedule.agents:
        model.sum_wages_households += i.wage
        model.sum_consumption_households += i.conso


def production(model):
    households_k = 0
    for i in model.schedule.agents:
        households_k += i.kapital
    model.production = model.techno*((households_k + model.bank.kapital + model.firm.kapital)**model.alpha)*(model.travail**(1 - model.alpha))
    return model.production

class BtcModel(Model):
    def __init__(self, n_households):
        self.n_households = n_households
        super().__init__()
        # Chose a schedule
        self.schedule = RandomActivation(self)
        self.production = 0
        self.kapital_households = [] 
        self.kapital_households_speculators = []
        self.sum_wages_households = 0
        self.sum_consumption_households = 0 
        self.sum_loans_households = 0
        self.travail = 100
        self.alpha = 0.5
        self.beta = 0.5
        self.techno = 1.3 # technology factor
        self.gamma = 0.67 # coefficient of production applie to salaries
        self.n = 12 

        self.start_datetime = datetime(2017, 1, 1,tzinfo=None)
        self.current_datetime = self.start_datetime

        self.datacollector = DataCollector(
            model_reporters={"Production": production},
            agent_reporters={"Wage": "wage"})

        # Create  a bank, a firm and n household
        self.firm = Firm(2, self)
        self.bank = Bank(1, self) 
          
        xh = risk_high_rate*self.n_households
        xm = xh + risk_medium_rate*self.n_households
        xl = xm + risk_low_rate*self.n_households
        for i in range(self.n_households):
            if i < xh:
                h = Household(i+2, 2, 0.45, self)
                self.schedule.add(h)
            elif i >= xh and i < xm:
                h = Household(i+2, 1, 0.2, self)
                self.schedule.add(h)
            elif i >= xm and i < xl:
                h = Household(i+2, 0, 0.05, self)
                self.schedule.add(h)
            else:
                h = Household(i+2, -1, 0, self)
                self.schedule.add(h)
        
        #Init production with kapital initialisation of agents and give loans
        production(self)
        self.bank.give_loan()

    def step(self):
        before_datetime = self.current_datetime
		# Update the current_datetime
        self.current_datetime = addMonth(before_datetime)
        # Collect data
        self.datacollector.collect(self)
        # Tell all the agents in the model to run their step function
        self.schedule.step()
        increase_wages_households(self)
        self.firm.step()
        increase_kapital_households(self)
        self.bank.step()
        production(self)
    
def addMonth(source):
    month = source.month
    year = source.year + month // 12
    month = source.month % 12 + 1
    return datetime(year,month,1)

        
        
        


