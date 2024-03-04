import pathlib
import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\agents"
from tqdm import tqdm
import phase1_agents as ag

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

def execute_interactions(listA, listB, *args, progress=True):
    data=[]
    range_iteractions = [args[0]] if type(args[0]) == int else args[0]
    for num_iteractions in tqdm(range_iteractions) if progress else range_iteractions:
        for i in tqdm(listA) if type(args[0])== int and progress else listA:
            for j in listB:
                i.reset()
                j.reset()
                inter = Interaction(i, j)
                for n in range(num_iteractions):
                    inter.execution()
                data.append([
                    num_iteractions,
                    i.get_name(),
                    i.get_points(),
                    j.get_name(),
                    j.get_points()
                    # i.get_memory(),
                ])
                if len(args)>1:
                    data[len(data)-1].append(args[1])
    return data

def optimize(agent, num_iteractions, agent_values):
    data=[]
    agentsB=ag.get_agents()

    for i in tqdm(agent_values):
        agentsA=ag.get_agents(agent)
        if agent == 'Selfish Difference':
            aux_agent = ag.SelfishDifference(i)
        elif agent == 'Middle Man':
            aux_agent = ag.MiddleMan(i)
        agentsA.append(aux_agent)

        aux= execute_interactions(agentsA, agentsB, num_iteractions, progress=False)
        for line in aux:
            data.append(line)
    return [data, agent]