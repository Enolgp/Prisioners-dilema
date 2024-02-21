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

from master_phase import execution, Interaction
import phase1_agents as ag
import tracker as trk

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
patata=trk.Tracker_multi_execution()

patata.add_data([10,'hernesto',100,'luisa',58,[1,0,0,1],[1,1,1,1]])
patata.add_data([11,'hernesto',100,'luisa',58,[1,0,0,1],[1,1,1,1]])
patata.add_data([12,'hernesto',100,'luisa',58,[1,0,0,1],[1,1,1,1]])
patata.add_data([13,'hernesto',100,'luisa',58,[1,0,0,1],[1,1,1,1]])
print(patata.show_data())