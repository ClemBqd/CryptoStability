from mesa import Agent
from household import rk

reserve_percent = 0.1

class Bank(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)
        self.loan = []
        self.deposits = 0
        self.reserves = 0


    def step(self):

        pass
