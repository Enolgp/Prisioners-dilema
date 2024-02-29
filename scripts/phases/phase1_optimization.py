import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.append(s+"\\agents")
sys.path.append(s+"\\data")
sys.path.append(s+"\\phases")

from master_phase import execute_interactions
import phase1_agents as ag
import tracker as trk
import pandas as pd

data=[]
agentsB=ag.get_agents()

# make a function of this
for i in range(10,100, 10):
    agentsA=ag.get_agents()
    agA = ag.SelfishDifference(i)
    print(len(agentsA))
    for a in agentsA:
        s+=a.get_name()
    print(s)
    aux= execute_interactions(agentsA, agentsB, 500)
    for line in aux:
        data.append(line)

print(pd.DataFrame(data))
trk.agent_optimization(data, 'Selfish Difference')