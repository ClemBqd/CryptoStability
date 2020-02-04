from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from datetime import datetime, timedelta
from household import Household
from bank import Bank, rate_loan_h, rk
from firm import Firm
import pandas as pd

risk_high_rate = 0.1
risk_medium_rate = 0.2
risk_low_rate = 0.2
P2 = 0.45 # propension to speculate risk high
P1 = 0.2 # risk medium
P0 = 0.05 # risk low

def kapital_new(model):
    households_k = 0
    for i in model.schedule.agents:
        households_k += i.kapital
    return households_k

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
    

def increase_wages_households(model):
    model.sum_wages_households = 0
    model.sum_consumption_households = 0
    for i in model.schedule.agents:
        model.sum_wages_households += i.wage
        model.sum_consumption_households += i.conso
    return model.sum_wages_households

def production(model):
    households_k = 0
    for i in model.schedule.agents:
        households_k += i.kapital
    model.production = model.techno*((model.firm.kapital+ households_k + model.bank.kapital)**model.alpha)*(model.travail**(1 - model.alpha)) #households_k + model.bank.kapital
    return model.production

def get_kapital_h(model):
    model.sum_speculator_portfolio = 0
    model.kh = 0
    model.kh_high = 0
    model.kh_medium = 0
    model.kh_low = 0
    for i in model.schedule.agents:
        if i.P == P0:
            model.kh_low += i.kapital
            model.sum_speculator_portfolio += i.speculator_portfolio
        elif i.P == P1:
            model.kh_medium += i.kapital
            model.sum_speculator_portfolio += i.speculator_portfolio
        elif i.P == P2:
            model.kh_high += i.kapital
            model.sum_speculator_portfolio += i.speculator_portfolio
        else:
            model.kh += i.kapital

def graph_households_kapital(model):
    a=0
    for i in range(model.n_households+2):
        if i >= 3:
            a += model.schedule.agents[i].kapital
            return a

def graph_households_wage(model):
    b = 0
    for i in range(model.n_households+2):
        if i >= 3:  
            b += model.schedule.agents[i].wage
            return b

def evolution_kapital_global(model):
    model.kapital_global = (1 + rk/model.n)*(model.kh_low*(1-P0) + model.kh_medium*(1-P1) + model.kh_high*(1-P2) + model.kh) + model.sum_wages_households - model.sum_consumption_households + model.sum_speculator_portfolio - model.sum_loans_households/(3*model.n)- model.sum_loans_households*rate_loan_h/model.n 
    model.kapital_global_btcModel.append(model.kapital_global)
    return model.kapital_global

def graph_kapital_bank(model):
    return model.bank.kapital

def graph_kapital_firm(model):
    return model.firm.kapital

class BtcModel(Model):
    def __init__(self, n_households, df3):
        self.n_households = n_households
        self.df3 = pd.read_excel(df3)
        super().__init__()
        # Chose a schedule
        self.schedule = RandomActivation(self)
        self.production = 0
        self.kapital_households = [] 
        self.kapital_households_speculators = []
        self.kapital_global_btcModel = []
        self.kh_high = 0
        self.kh_medium = 0
        self.kh_low = 0
        self.kh = 0
        self.sum_speculator_portfolio = 0
        self.sum_wages_households = 0
        self.sum_consumption_households = 0 
        self.sum_loans_households = 0
        self.travail = 1000
        self.alpha = 0.5
        self.beta = 0.5
        self.techno = 1.3 # technology factor
        self.gamma = 0.6 # coefficient of production applie to salaries 0.67
        self.n = 12 

        self.start_datetime = datetime(2017, 1, 1,tzinfo=None)
        self.current_datetime = self.start_datetime

        self.datacollector = DataCollector(
            model_reporters={"Production": production,
                            "KapitalG": evolution_kapital_global,
                            "KapitalH": kapital_new,
                            "WagesH" : graph_households_wage,
                            "sum_wage":increase_wages_households,
                            "KapitalF": graph_kapital_firm,
                            "KapitalB": graph_kapital_bank,
                            "diff": diff},
            agent_reporters={"Wage": "wage"})
        self.running = True
        
        # Create  a bank, a firm and n household
        self.firm = Firm(2, self)
        self.bank = Bank(1, self) 
          
        xh = risk_high_rate*self.n_households
        xm = xh + risk_medium_rate*self.n_households
        xl = xm + risk_low_rate*self.n_households
        for i in range(self.n_households):
            if i < xh:
                h = Household(i+2, 2, P2, self)
                self.schedule.add(h)
            elif i >= xh and i < xm:
                h = Household(i+2, 1, P1, self)
                self.schedule.add(h)
            elif i >= xm and i < xl:
                h = Household(i+2, 0, P0, self)
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
        get_kapital_h(self)
        # Tell all the agents in the model to run their step function
        self.schedule.step()
        evolution_kapital_global(self)
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
        

def diff(model):
    a=0
    model.sum_wages_households = 0
    model.sum_consumption_households = 0
    for i in model.schedule.agents:
        model.sum_wages_households += i.wage
        model.sum_consumption_households += i.conso
    a=model.sum_wages_households-model.sum_consumption_households
    return a

class SinuModel(BtcModel):
    def __init__(self, n_households, df3, list_kapital_global):
        BtcModel.__init__(self, n_households, df3)
        self.list_kapital_global = list_kapital_global
        self.R = []
        self.i = 0

    def calcul_taux(self):
        R=-1+(self.list_kapital_global[self.i]-(self.sum_wages_households - self.sum_consumption_households + self.sum_speculator_portfolio - self.sum_loans_households/(3*self.n)- self.sum_loans_households*rate_loan_h/self.n ))/(self.kh_low*(1-P0) + self.kh_medium*(1-P1) + self.kh_high*(1-P2) + self.kh)
        self.R.append(R)
        self.i += 1

    def step(self):
        before_datetime = self.current_datetime
		# Update the current_datetime
        self.current_datetime = addMonth(before_datetime)
        # Collect data
        self.datacollector.collect(self)
        get_kapital_h(self)
        # Tell all the agents in the model to run their step function
        self.schedule.step()
        evolution_kapital_global(self)
        increase_wages_households(self)
        self.firm.step()
        increase_kapital_households(self)
        self.bank.step()
        production(self)
     