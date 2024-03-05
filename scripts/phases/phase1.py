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

from master_phase import execute_interactions, comparation_no_equitative
import phase1_agents as ag
import tracker as trk

agentsA = ag.get_agents()
agentsB = ag.get_agents()

# comparative graph
compare_data =execute_interactions(agentsA, agentsB, 100)
trk.show_comparation(compare_data, 'Comparation_phase1', overwrite=False)
# trk.save_csv(compare_data, 'Comparation_phase1')
# graph ov evolutions
evol_data = execute_interactions(agentsA, agentsB, range(1, 30))
trk.show_evolution(evol_data, 'Evolution_phase1', overwrite=False)
trk.show_evolution(evol_data, 5, 'Evolution_phase1', overwrite=False)
# trk.save_csv(evol_data, 'Evolution_phase1')

# study the behaviour of each agent when facing the mayority each type of agent
data_no_equi = comparation_no_equitative(500)
trk.show_table(data_no_equi, 'numeric', overwrite=False)
trk.show_table(data_no_equi, 'color-desc', overwrite=False)
trk.show_table(data_no_equi, 'color', overwrite=False)