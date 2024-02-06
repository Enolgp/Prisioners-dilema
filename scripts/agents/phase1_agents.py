from Agent import Agent
import random
import numpy as np

def get_agents():
    agents = [
        TipForTap(),
        Random(),
        AlwaysColab(),
        NeverColab(),
        Trigger(),
        Pavlov(),
        ForgivingTipForTap(),
        Spiteful(),
        ReverseTipForTap(),
        Mayority(),
        MiddleMan(),
        Tentated(),
        ShortTimeMemomry(),
        RandomDataSample()
    ]
    return agents

class TipForTap(Agent):
    def __init__(self):
        super().__init__("Tip fot Tap")

    def strategy(self):
        '''
        It starts colaborating and in the following interactions it repeats
        the rival's last election
        '''
        if len(self.memory)==0:
            return 1
        return self.memory[len(self.memory)-1][1]

class Random(Agent):
    def __init__(self):
        super().__init__("Random")

    def strategy(self):
        '''
        In each iteraction there are a 50% chances of colaborate
        '''
        return random.randint(0,1)
    
class AlwaysColab(Agent):
    def __init__(self):
        super().__init__("Always colaborate")

    def strategy(self):
        '''
        Always colaborates
        '''
        return 1
    
class NeverColab(Agent):
    def __init__(self):
        super().__init__("Never Colaborate")

    def strategy(self):
        '''
        Never colaborates
        '''
        return 0

class Trigger(Agent):
    def __init__(self):
        super().__init__("Trigger")

    def strategy(self):
        '''
        It starts colaborating and keep doing it until the rival doesn't colaborate
        then it always doesn't colaborate
        '''
        betrayal = False
        if len(self.memory) == 0:
            return 1
        else:
            if self.memory[-1][1] == 0:
                betrayal=True
            return 0 if betrayal else 1
        
class Pavlov(Agent):
    def __init__(self):
        super().__init__("Pavlov")

    def strategy(self):
        '''
        It starts colaborating but it changes the action if the last 
        iteranction the rival and it didn't did the same election
        '''
        if len(self.memory)==0:
            return 1
        else:
            if self.memory[-1][0] == self.memory[-1][1]:
                return self.memory[-1][0]
            return self.memory[-1][1]
            
class ForgivingTipForTap(Agent):
    def __init__(self):
        super().__init__("Forgiving Tip For Tap")

    def strategy(self):
        '''
        It starts colaborating and it repeats the same action the enemy did the
        last turn with condition that if the rival didnt colaborate the last 3
        interactions, the agent will forgive it and collaborate
        '''
        counter=0
        if len(self.memory)==0:
            return 1
        if self.memory[-1][1] == 0:
            arr = np.array(self.memory[-3:])
            n=arr.sum(axis=0)[1]
            if n>0:
                return 0
            return 1
        return 1

class Spiteful(Agent):
    def __init__(self):
        super().__init__("Spiteful")

    def strategy(self):
        '''
        It starts colaborating and if the enemie obtain more points than it
        the agent will allways no collaborate from then on
        '''
        betrayal=False
        if len(self.memory)==0:
            return 1 
        if betrayal:
            return 0
        if self.memory[-1][0] != self.memory[-1][1] and self.memory[-1][0] == 1:
            betrayal=True
            return 0
        return self.memory[-1][1]
    
class ReverseTipForTap(Agent):
    def __init__(self):
        super().__init__("Reverse Tip For Tap")

    def strategy(self):
        '''
        It starts not colaborating and in the sucesive iteractions it repeats
        the enemie's last election
        '''
        if len(self.memory)==0:
            return 0
        return self.memory[-1][1]
    
class Mayority(Agent):
    def __init__(self):
        super().__init__("Mayority")

    def strategy(self):
        '''
        It starts colaborating and in the next iteractions it does the
        most common action the rival did in the hole history of iteractions
        '''
        arr = np.array(self.memory)
        if len(self.memory)==0:
            return 1
        if (arr.sum(axis=0)[1])/len(self.memory) <= 0.5:
            return 0
        return 1
    
class MiddleMan(Agent):
    '''
    Colaborates as long as the rival has colaborated between the 20 and 80 %
    of the times. Otherwise it don't colaborate in the logic that:
    >80% its likely to obtain more benefict
    <20% its not likely to obtanin benefict
    '''
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

class Tentated(Agent):
    def __init__(self):
        super().__init__("Tentated")
    
    def strategy(self):
        '''
        There is a random probability of no coperation although this probability is
        influenced by the number of times the rival has cooperated 
        '''
        temptation=0
        if len(self.memory) == 0:
            return 1

        for n in self.memory:
            if n[1] == 1:
                temptation+=1 if temptation<10 else 10
            else:
                temptation-=1 if temptation>0 else 0

        x = random.random()/2+0.1*temptation
        return 1 if x<0.9 else 0

class ShortTimeMemomry(Agent):
    def __init__(self):
        super().__init__("Short time memory")

    def strategy(self):
        '''
        Return the most common election in the last 25 rival's elections
        '''
        if len(self.memory)==0:
            return 1
        arr=np.array(self.memory[-25:])
        x =arr.sum(axis=0)[1]
        if x < 5:
            return 0
        return 1
    
class RandomDataSample(Agent):
    def __init__(self):
        super().__init__("Random data sample")

    def strategy(self):
        '''
        Starts colaborating and in the next interactions selects a data sample 
        formed for a random number of radom rival's elections and return the 
        most common election in that sample
        '''
        arr=[]
        if len(self.memory) == 0:
            return 1

        n = random.randint(1,len(self.memory)-1) if len(self.memory)>3 else 2
        for i in range(n):
            arr.append(self.memory[random.randint(0, len(self.memory)-1)][1])
        if sum(arr)/n > 0.5:
            return 1
        return 0