import Agent
import random

class Random(Agent):
    def strategy(self):
        return random.randint(0,1)