import sys
import pathlib
s=str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.append(s+"\\agents")
sys.path.append(s+"\\data")
sys.path.append(s+"\\phases")    

from master_phase import optimize
import phase1_agents as ag
import tracker as trk
import pandas as pd

optimizeDiff = optimize('Selfish Difference', 2000, range(10,80,10))
trk.agent_optimization(optimizeDiff[0], optimizeDiff[1])

rangeMiddleMan=[]
for i in range(0, 50,10):
    for j in range(100, 49, -10):
        rangeMiddleMan.append([i,j])
optimizeDiff = optimize('Middle Man', 500, rangeMiddleMan)
trk.agent_optimization(optimizeDiff[0], optimizeDiff[1])
