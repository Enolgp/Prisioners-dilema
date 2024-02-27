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

from master_phase import execute_interactions
import phase1_agents as ag
import tracker as trk

agentsA = ag.get_agents()
agentsB = ag.get_agents()

# comparative graph
trk.show_comparation(execute_interactions(agentsA, agentsB, 50))
# graph ov evolutions
evol_data = execute_interactions(agentsA, agentsB, range(100, 201, 10))
trk.show_evolution(evol_data)
trk.show_evolution(evol_data, 3)

# study the behaviour of each agent when facing the mayority each type of agent
