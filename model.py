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
    kh = 0
    khp = 0
    for i in model.schedule.agents:
        if i.risk_profile == -1:
            kh += i.kapital
            model.kapital_households.append(kh)
        else:
            khp += i.kapital
            model.kapital_households_speculators.append(khp)

# def increase_sum_consumption_households to docomme au dessusu

class BtcModel(Model):
    def __init__(self, n_households):
        self.n_households = n_households
        super().__init__()
        # Chose a schedule
        self.schedule = RandomActivation(self)
        self.production = 10
        self.kapital_households = [] # To change in a list of the sum 
        self.kapital_households_speculators = [] # # To change in a list of the sum
        self.sum_loans_households = self.n_households*loan_households
        self.sum_wages_households = 0
        self.sum_consumption_households = 0 
        self.travail = 100
        self.alpha = 0.5
        self.beta = 0.5
        self.techno = 1.3 # technology factor
        #self.daypassed = False
		self.monthpassed = False

		# Attributes related to time
		self.start_datetime = datetime(2017, 1, 1, 0, 0, 0, tzinfo=None)
		self.current_datetime = self.start_datetime
		self.step_interval = "month"

        #part relatives to time 
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
        
        # Put variable comun of all the model too
    def time_tick(self, before_datetime):
        if before_datetime.month != self.current_datetime.month:
            self.monthpassed = True
        else:
            self.monthpassed = False


    def step(self):
        # Tell all the agents in the model to run their step function
        before_datetime = self.current_datetime
		# Update the current_datetime
		self.current_datetime = support_classes.addMonth(self.current_datetime)
		# Check if a new day passed
		self.time_tick(before_datetime)
        self.datacollector.collect(self)
        self.schedule.step()
        increase_kapital_households(self)
        #self.bank.step()
        # Collect data
        


