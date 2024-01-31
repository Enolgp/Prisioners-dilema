from master_phase import Interaction
import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
s+="\\agents"
sys.path.append(s)
from phase1_agents import *

TFT = TipForTap()
RAN = Random()

inte = Interaction(TFT, RAN)
for i in range(1000):
    inte.execution()

print(TFT.get_points())