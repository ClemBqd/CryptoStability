from mesa import Agent
from bank import rate_loan_f

increasing_rate = 2.5/100 #pourcentage surement 

class Firm(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id,model)
        self.kapital = 1500
        self.loan = 0

    def evolution(self):
        self.kapital = self.kapital*increasing_rate/self.model.n - self.model.sum_wages_households + self.model.sum_consumption_households - self.loan*(1/(self.model.n*3) + rate_loan_f/self.model.n)
        return self.kapital

    def step(self):
        
        self.evolution()