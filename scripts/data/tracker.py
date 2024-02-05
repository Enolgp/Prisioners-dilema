import csv
import json

class Tracker():
    data = []

    def get_data(self):
        return self.data
    
    def add_data(self, agent1, agent2):
        new_data=[
            [agent1.get_name(), agent1.get_points(), agent1.get_memory()],
            [agent2.get_name(), agent2.get_points(), agent2.get_memory()],
        ]
        self.data.append(new_data)

    def save_data(self, name):
        with open(f"data/{name}.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)