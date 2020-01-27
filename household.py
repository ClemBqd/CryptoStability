from mesa import Agent
from bank import rk, rate_loan_h
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


P = 0.1 #Propertion to speculate
gamma = 0.67 # coefficient of production
loan_households = 100
df3 = pd.read_excel('pfebtc.xltx') 

class Household(Agent):
    def __init__(self, unique_id, risk_profile, model):
        self.unique_id = unique_id
        self.risk_profile = risk_profile # -1 for risk_averse 1 for risk_lover and later 0 for risk_neutral
        super().__init__(unique_id, model)
        self.wage = 10 #salary month
        self.kapital = 0 + loan_households + self.wage
        self.conso = 10
        self.speculator_portfolio = 10.0
        self.loan = loan_households
        
    def kapital_evolution(self):
        self.kapital = (1 - rk)*self.kapital + self.wage - self.conso - self.loan*(1 + rate_loan_h)
        
        return self.kapital
    
    def speculator_ptf(self):

        if self.risk_profile != -1:
            self.speculator_portfolio = self.speculator_portfolio*(1 +df3['variation'][df3.loc[df3['Date'] == self.model.current_datetime].index.item()]) + P*self.kapital
        return self.speculator_portfolio
    
    def consumption(self):
        if self.risk_profile == -1:
            self.conso = self.model.techno*(self.kapital**self.model.alpha)*(self.model.travail**(1-self.model.alpha))*(1 - self.model.alpha*self.model.beta)
        else:
            self.conso = self.model.techno*((self.kapital + self.speculator_portfolio)**self.model.alpha)*(self.model.travail**(1-self.model.alpha))*(1 - self.model.alpha*self.model.beta)
        

    def receive_salary(self):
        self.wage = (1 - gamma)*self.model.production
        self.model.sum_wages_households += self.wage*self.model.n_households
        return self.wage

    def step(self):
        self.speculator_ptf()
        self.receive_salary()
        self.consumption()
        self.kapital_evolution()
        
        
        
        
