class Interaction:
    Agent1 = None
    Agent2 = None
    
    def __init__(self, n) -> None:
        self.num = n

    def pointDistribution(self, ElectionAgent1, ElectionAgent2):
        if ElectionAgent1 == 1 and ElectionAgent2 == 1:
            self.Agent1.add_points(3)
            self.Agent2.add_points(3)
        elif ElectionAgent1 == 1 and ElectionAgent2 == 0:
            self.Agent1.add_points(0)
            self.Agent2.add_points(5)
        elif ElectionAgent1 == 0 and ElectionAgent2 == 1:
            self.Agent1.add_points(5)
            self.Agent2.add_points(0)
        elif ElectionAgent1 == 0 and ElectionAgent2 == 0:
            self.Agent1.add_points(1)
            self.Agent2.add_points(1)
    
    # def execution(self):