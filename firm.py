from mesa import Agent
from bank import rate_loan_f

increasing_rate = 2.5

class Firm(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id,model)
        self.kapital = 1500
        self.loan = 0

    def evolution(self):
        self.kapital += self.kapital*increasing_rate + self.model.sum_wages_households - self.model.sum_consumption_households - self.loan*(1 + rate_loan_f)
        return self.kapital

    def step(self):

        self.evolution()