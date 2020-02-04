from mesa import Agent
from bank import rk, rate_loan_h
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

#df3 = pd.read_excel('pfebtc.xlsx') 

class Household(Agent):
    def __init__(self, unique_id, risk_profile, P, model):
        self.unique_id = unique_id
        self.risk_profile = risk_profile # -1 for risk_averse 2 for risk_high and 1 for risk_medium 0 for risk_low
        self.P = P # Propertion to speculate
        super().__init__(unique_id, model)
        self.df3 = self.model.df3
        self.wage = 0 #salary month
        self.conso = 0
        self.speculator_portfolio = 0
        self.loan = 0
        self.kapital = 0
        
    def kapital_evolution(self):
        if self.risk_profile != -1:
            self.kapital = (1 + rk/self.model.n)*self.kapital*(1-self.P) + self.wage - self.conso - self.loan/(10*self.model.n)- self.loan*rate_loan_h/self.model.n+self.speculator_portfolio
        else:    
            self.kapital = (1 + rk/self.model.n)*self.kapital + self.wage - self.conso - self.loan/(10*self.model.n)- self.loan*rate_loan_h/self.model.n
        return self.kapital
    
    def speculator_ptf(self):
        if self.risk_profile != -1:
            self.speculator_portfolio = self.P*self.kapital*(1 +self.df3['variation'][self.df3.loc[self.df3['Date'] == self.model.current_datetime].index.item()])
        return self.speculator_portfolio
    
    def consumption(self):
        self.conso = 0.50 * self.kapital #self.model.techno*((self.kapital)**self.model.alpha)*((self.model.travail/self.model.n_households)**(1-self.model.alpha))*(1 - self.model.alpha*self.model.beta)
        
    def receive_salary(self):
        self.wage = (1 - self.model.gamma)*self.model.production/self.model.n_households
        return self.wage
    

    def step(self):
        self.speculator_ptf()
        self.receive_salary()
        self.consumption()
        self.kapital_evolution()
        
        
        
        
