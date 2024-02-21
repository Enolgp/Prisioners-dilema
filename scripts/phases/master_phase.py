import sys
import pathlib

class Interaction:
    Agent1 = None
    Agent2 = None
    
    def __init__(self, ag1, ag2) -> None:
        self.Agent1 = ag1
        self.Agent2 = ag2

    def pointDistribution(self, ElectionAgent1, ElectionAgent2):
        if ElectionAgent1 == 1 and ElectionAgent2 == 1:
            self.Agent1.add_points(3)
            self.Agent2.add_points(3)
        elif ElectionAgent1 == 1 and ElectionAgent2 == 0:
            self.Agent1.add_points(0)
            self.Agent2.add_points(5)
        elif ElectionAgent1 == 0 and ElectionAgent2 == 1:
            self.Agent1.add_points(5)
            self.Agent2.add_points(0)
        elif ElectionAgent1 == 0 and ElectionAgent2 == 0:
            self.Agent1.add_points(1)
            self.Agent2.add_points(1)

    def saveInMemory(self, electionAgent1, electionAgent2):
        self.Agent1.add_to_memory([electionAgent1, electionAgent2])
        self.Agent2.add_to_memory([electionAgent2, electionAgent1])
    
    def execution(self):
        agent1election = self.Agent1.strategy()
        agent2election = self.Agent2.strategy()

        self.saveInMemory(agent1election, agent2election)
        self.pointDistribution(agent1election, agent2election)

def execution(listA, listB, tracker, num):
    for i in listA:
        for j in listB:
            i.reset()
            j.reset()
            int = Interaction(i, j)
            for n in range(num):
                int.execution()
            tracker.add_data(agent1=i, agent2=j)