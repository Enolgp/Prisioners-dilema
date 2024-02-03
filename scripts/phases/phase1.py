from master_phase import Interaction
import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\agents"
sys.path.append(s)
from phase1_agents import *

agents=phase1_agents.get_agents()
num_interactions = 1000

for i in agents:
    for j in agents:
        int = Interaction(i, j)
        for n in range(num_interactions):
            int.execution()