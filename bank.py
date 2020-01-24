from mesa import Agent


reserve_percent = 0.1
rk = 0.01 # deposit rate

class Bank(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)
        self.loan = []
        self.deposits = 0
        self.reserves = 0


    def step(self):

        pass
