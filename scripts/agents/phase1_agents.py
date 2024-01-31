from Agent import Agent
import random

class TipForTap(Agent):    
    def strategy(self):
        if len(self.memory)==0:
            return 1
        else:
            return self.memory[len(self.memory)-1][1]

class Random(Agent):
    def strategy(self):
        return random.randint(0,1)