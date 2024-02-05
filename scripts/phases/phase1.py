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
from tracker import Tracker

trk = Tracker()
agentsA=get_agents()
agentsB=get_agents()
num_interactions = 500

for i in agentsA:
    for j in agentsB:
        i.reset()
        j.reset()
        int = Interaction(i, j)
        for n in range(num_interactions):
            int.execution()
        trk.add_data(agent1=i, agent2=j)
        trk.save_data("Phase1")