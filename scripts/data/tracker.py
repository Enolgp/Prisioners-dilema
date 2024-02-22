import csv
import pandas as pd
import matplotlib.pyplot as plt

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

    def show_data(self):
        df=pd.DataFrame(self.data)

        df['agent_1'] = df[0].apply(lambda x: x[0])
        df['agent_2'] = df[1].apply(lambda x: x[0])
        df['points_1'] = df[0].apply(lambda x: x[1])
        df['points_2'] = df[1].apply(lambda x: x[1])

        df = df[['agent_1', 'points_1','agent_2', 'points_2']]
        print(df)
        
        averages = round(df.groupby(['agent_1'])['points_1'].mean().sort_values(), 2)
        print(averages)
        plt.barh(averages.index, averages.values)
        plt.show()

class Tracker_multi_execution():
    data=[]

    def get_data(self):
        return self.data
    
    def save_data(self, name):
        with open(f"data/{name}.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    # def add_data(self, agent1, agent2, num):
    #     new_data=[
    #         num,
    #         [agent1.get_name(), agent1.get_points(), agent1.get_memory()],
    #         [agent2.get_name(), agent2.get_points(), agent2.get_memory()],
    #     ]
    #     self.data.append(new_data)
            
    def add_data(self, num, agent1, agent2):
        self.data.append([
            num,
            agent1.get_name(),
            agent1.get_points(),
            agent2.get_name(),
            agent2.get_points()
        ])

    def show_data(self):
        df=pd.DataFrame(self.data)

        df['num_iteractions'] = df[0]
        df['agent_1'] = df[1]
        df['agent_2'] = df[3]
        df['points_1'] = df[2]
        df['points_2'] = df[4]

        df = df[['num_iteractions','agent_1', 'points_1']]

        averages = round(df.groupby(['agent_1','num_iteractions'])['points_1'].mean().reset_index(), 2)
        averages = averages.rename(columns={'points_1':'average'})

        for agent in averages['agent_1'].unique():
            df_agent = averages[averages['agent_1']==agent]
            plt.plot(df_agent['num_iteractions'], df_agent['average'], label=agent)
        
        plt.xlabel("Num-Iteractions")
        plt.ylabel("Averages")
        plt.title('Evolution with number of iteractions')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()