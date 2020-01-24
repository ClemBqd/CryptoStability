from mesa import Agent

rate_loan = 0.1 # if the rate_loan is the variable that is impacted by the econimic cycle -> to put in model.py file
increasing_rate = 2.5
loan_firm = 0

class Firm(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id,model)
        self.kapital = 0 + loan_firm

    def evolution(self):
        
        self.kapital = self.kapital*increasing_rate - loan_firm*(1 + rate_loan)
        # Add consumption of households and take of wage
        return self.kapital

    def step(self):

        self.evolution()