class Agent:
    memory = []
    points = 0
    
    def __init__(self, name):
        self.name = name
    
    def get_points(self):
        return self.points
    
    def get_memory(self):
        return self.memory
    
    def set_memory(self, mem):
        self.memory = mem

    def add_to_memory(self, data):
        self.memory.append(data)
    
    def get_name(self):
        return self.name

    def add_points(self, n):
        self.points += n
    
    def reset(self):
        self.points = 0
        self.memory = []