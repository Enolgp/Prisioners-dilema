from Agent import Agent
import random

class TipForTap(Agent):
    def __init__(self) -> None:
        super().__init__("Tip For Tap")
    def strategy(self):
        if len(self.memory)==0:
            return 1
        else:
            return self.memory[len(self.memory)-1][1]

class Random(Agent):
    def __init__(self) -> None:
        super().__init__("Random")
    def strategy(self):
        return random.randint(0,1)
    
def get_agents(self):
    tfp = TipForTap()
    ran = Random()
    agents = [tfp, ran]
    return agents