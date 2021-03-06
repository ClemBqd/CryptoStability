from mesa import Agent

reserve_percent = 0.1
rk = 0.01 # deposit rate of households
rate_loan_f = 0.005 # rate loan of firm
rate_loan_h = 0.05 # rate loan of households

class Bank(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)
        self.kapital = 10000
        

    def give_loan(self):
        loan_households = ((1 - self.model.gamma)*self.model.production)*5
        self.model.firm.loan = 0.5*self.model.firm.kapital
        self.model.firm.kapital += self.model.firm.loan
        self.kapital -= self.model.firm.loan
        for i in self.model.schedule.agents:
            i.kapital += loan_households/self.model.n_households
            i.loan = loan_households/self.model.n_households
            self.model.sum_loans_households += loan_households/self.model.n_households

        self.kapital -= loan_households   
        self.model.kapital_global += self.model.sum_loans_households 
        
    def evolution(self):
        kh = len(self.model.kapital_households)
        khp = len(self.model.kapital_households_speculators)
        self.kapital = self.model.kapital_households[kh-1] - (rk/self.model.n)*self.model.kapital_households[kh-2] + self.model.kapital_households_speculators[khp-1] - (rk/self.model.n)*self.model.kapital_households_speculators[khp-2] + self.model.sum_loans_households*(1/(self.model.n)*3 + rate_loan_h/self.model.n) + self.model.firm.loan*(1/(self.model.n*3) + rate_loan_f/self.model.n)

    def step(self):
        self.evolution()
