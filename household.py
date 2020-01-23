from mesa import Agent

ispe = 0.1 # Cours du bitcoin - à add en argument step function
P = 0.1 #Propertion to speculate
rk = 0.1 #To define
sp = 0.1 #To define = %of kapital speculators
techno = 0.5 # technology factor - Z
rate_loan = 0.1 # if the rate_loan is the variable that is impacted by the econimic cycle -> to put in model.py file
gamma = 0.1 # coefficient of production
loan_households = 100
# self.bank ? 

class Household(Agent):
    def __init__(self, unique_id, risk_profile, model):
        self.unique_id = unique_id
        self.risk_profile = risk_profile # -1 for risk_averse 1 for risk_lover and later 0 for risk_neutral
        super().__init__(unique_id, model)
        self.wage = 10 #salary month
        self.debt = 10
        self.kapital = 0 + loan_households
        self.conso = 10
        
        self.speculator_portfolio = 10.0 
        
    def kapital_evolution(self):
        if self.risk_profile == -1:
            self.kapital = (1 - rk)*self.kapital + self.wage - self.conso - loan_households*(1 + rate_loan)
        else:
            self.kapital = (1 - sp + rk)*self.kapital + self.wage - self.conso - loan_households*(1 + rate_loan)
        return self.kapital
    
    def speculator_ptf(self):
        if self.risk_profile == 1:
            self.speculator_portfolio = self.speculator_portfolio*(1 + ispe) + P*self.kapital
        return self.speculator_portfolio
    
    def consumption(self):
        if self.risk_profile == -1:
            self.conso = techno*(self.kapital**self.model.alpha)*(self.model.travail**(1-self.model.alpha))*(1 - self.model.alpha*self.model.beta)
        else:
            self.conso = techno*((self.kapital + self.speculator_portfolio)**self.model.alpha)*(self.model.travail**(1-self.model.alpha))*(1 - self.model.alpha*self.model.beta)
        # self.kapital -= self.conso

    def receive_salary(self):
        self.wage = (1 - gamma)*self.model.production
        # self.capital += self.wage
        return self.wage

    def step(self):
        
        self.kapital_evolution()
        self.speculator_ptf()
        self.consumption()
        self.receive_salary()
        
