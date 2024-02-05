from Agent import Agent
import random
import numpy as np

def get_agents():

    agents = [
        TipForTap(),
        Random(),
        Jesus(),
        Lucifer(),
        Trigger(),
        Pavlov(),
        ForgivingTipForTap(),
        Spiteful(),
        ReverseTipForTap(),
        Mayority(),
        MiddleMan()
    ]
    return agents

class TipForTap(Agent):
    def __init__(self):
        super().__init__("Tip fot Tap")

    def strategy(self):
        if len(self.memory)==0:
            return 1
        return self.memory[len(self.memory)-1][1]

class Random(Agent):
    def __init__(self):
        super().__init__("Random")

    def strategy(self):
        return random.randint(0,1)
    
class Jesus(Agent):
    def __init__(self):
        super().__init__("Jesus")

    def strategy(self):
        return 1
    
class Lucifer(Agent):
    def __init__(self):
        super().__init__("Lucifer")

    def strategy(self):
        return 0

class Trigger(Agent):
    def __init__(self):
        super().__init__("Trigger")

    def strategy(self):
        betrayal = False
        if len(self.memory) == 0:
            return 1
        else:
            if self.memory[-1][1] == 1:
                betrayal=True
            return 0 if betrayal else 1
        
class Pavlov(Agent):
    def __init__(self):
        super().__init__("Pavlov")

    def strategy(self):
        if len(self.memory)==0:
            return 0
        else:
            if self.memory[-1][0] == self.memory[-1][1]:
                return self.memory[-1][0]
            return self.memory[-1][1]
            
class ForgivingTipForTap(Agent):
    def __init__(self):
        super().__init__("Forgiving Tip For Tap")

    def strategy(self):
        counter=0
        if len(self.memory)==0:
            return 0
        if self.memory[-1][1] == 0:
            counter+=1
            if counter<=3:
                return 0
            return 1
        return 1

class Spiteful(Agent):
    def __init__(self):
        super().__init__("Spiteful")

    def strategy(self):
        betrayal=False
        if len(self.memory)==0:
            return 1 
        if betrayal:
            return 0
        if self.memory[-1][0] == self.memory[-1][1] and self.memory[-1][0] == 0:
            betrayal=True
            return 0
        return self.memory[-1][1]
    
class ReverseTipForTap(Agent):
    def __init__(self):
        super().__init__("Reverse Tip For Tap")

    def strategy(self):
        if len(self.memory)==0:
            return 0
        return self.memory[-1][1]
    
class Mayority(Agent):
    def __init__(self):
        super().__init__("Hard Mayority")

    def strategy(self):
        arr = np.array(self.memory)
        if len(self.memory)==0:
            return 1
        if (arr.sum(axis=0)[1])/len(self.memory) <= 0.5:
            return 0
        return 1
    
class MiddleMan(Agent):
    def __init__(self):
        super().__init__("Middle man")
    
    def strategy(self):
        arr = np.array(self.memory)

        if len(self.memory)==0:
            return 1
        
        x =arr.sum(axis=0)[1]/len(self.memory)
        if x >= 0.8 or x <= 0.2:
            return 0
        return 1
    
# idea: paciencia/tentación. utiliza contadores para ver si el rival 
    # lleva varias rondas colaborando o no colaborando