import Agent

class TipForTap(Agent):
    def __init__(self, tag):
        memory = self.get_memory()
    
    def strategy(self):
        if len(self.memory)==0:
            return 1
        else:
            return self.memory[len(self.memory)-1][1]