import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\agents"
sys.path.append(s)
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\data"
sys.path.append(s)
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\phases"
sys.path.append(s)

from master_phase import Interaction
import phase1_agents as ag
import tracker as trk
from tqdm import tqdm

agentsA = ag.get_agents()
agentsB = ag.get_agents()

def execution(listA, listB, *args):
    data=[]
    range_iteractions = [args[0]] if type(args[0]) == int else args[0]
    for num_iteractions in tqdm(range_iteractions):
        for i in listA:
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
                    j.get_points(),
                    i.get_memory(),
                ])
    return data

#comparative graph
trk.show_comparation(execution(agentsA, agentsB, 200))
#graph 
trk.show_evolution(execution(agentsA, agentsB, range(10, 151)))
#study the behaviour of each agent when facing the mayority each type of agent
