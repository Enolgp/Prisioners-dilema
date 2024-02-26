from master_phase import Interaction
import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\agents"
sys.path.append(s)
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\data"
sys.path.append(s)
from phase1_agents import *
from tracker2 import Tracker
import tqdm

trk = Tracker()
agentsA=get_agents()
agentsB=get_agents()
for i in range(15):
    agentsB.append(MiddleMan())
num_interactions = 1000


for i in agentsA:
    for j in agentsB:
        i.reset()
        j.reset()
        int = Interaction(i, j)
        for n in range(num_interactions):
            int.execution()
        trk.add_data(agent1=i, agent2=j)

# trk.save_data("Phase1")
trk.show_data()

# ====================================
# PHASE 1 EXTENDED
# ====================================

range_interactions = [100, 200]
range_interactions.append(range(500, 15000))

agentsA = ag.get_agents()
agentsB = ag.get_agents()

def comparation_fixed_number(n):
    tracker = trk.Tracker()
    for i in agentsA:
        for j in agentsB:
            i.reset()
            j.reset()
            int = Interaction(i, j)
            for n in range(n):
                int.execution()
            tracker.add_data(agent1=i, agent2=j)
    tracker.save_data("Phase1")
    tracker.show_data()

#testing
tracker=trk.Tracker_multi_execution()

def execution(listA, listB, tracker, num):
    for i in listA:
        for j in listB:
            i.reset()
            j.reset()
            int = Interaction(i, j)
            for n in tqdm(range(num)):
                int.execution()
            tracker.add_data(num, agent1=i, agent2=j)

for i in tqdm(range(10, 1010, 200), desc='los agentes interactuan entre si'):
    execution(agentsA, agentsB, tracker, i)

tracker.show_data()
# patata.add_data([10,'hernesto',105,'luisa',5,[1,0,0,1],[1,1,1,1]])