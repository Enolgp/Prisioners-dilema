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
from tqdm import tqdm
import pandas as pd
import os

agentsA = ag.get_agents()
agentsB = ag.get_agents()

data=[]
for agen in tqdm(agentsA):
    agentsB = ag.get_no_equitative_agents(agen.get_name())
    lst=[]
    for aux in agentsB:
        lst.append(aux.get_name())
    data.extend(execute_interactions(agentsA, agentsB, 50, agen.get_name(), progress=False))

trk.show_table(data, 'numeric', show=True, save=True, overwrite=False)
trk.show_table(data, 'color-desc', show=True, save=True, overwrite=False)
trk.show_table(data, 'color', show=True, save=True, overwrite=False)
print(os.path.exists(os.path.join('data/img', 'table_50_interactuions.png')))
print(os.listdir('data/img'))