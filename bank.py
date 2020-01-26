from mesa import Agent


reserve_percent = 0.1
rk = 0.01 # deposit rate of households
rate_loan_f = 0.01 # rate loan of firm
rate_loan_h = 0 # rate loan of households

class Bank(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)
        self.kapital = - model.sum_loans_households - model.firm.loan
        
    def evolution(self):
        # xh = len(self.model.kapital_households)
        # xhp = len(self.model.kapital_households_speculators)
        self.kapital = self.model.kapital_households[-1] - rk*self.model.kapital_households[-2] + self.model.kapital_households_speculators[-1] - rk*self.model.kapital_households_speculators[-2] + self.model.sum_loans_households*(1 - rate_loan_h) + self.model.firm.loan*(1 - rate_loan_f)

    def step(self):

        self.evolution()
