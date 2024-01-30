class Agent:
    memory = []
    points = 0
    def __init__(self) -> None:
        pass
    
    def get_points(self):
        return self.points
    
    def get_memory(self):
        return self.memory
    
    def set_memory(self, mem):
        self.memory = mem
    
    def add_points(self, n):
        self.points += n