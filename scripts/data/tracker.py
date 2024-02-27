import csv
import pandas as pd
import matplotlib.pyplot as plt

'''
Recieve a list(1) of list(2) where the list 2 is like:
[
number of iteractions,
name of agent 1,
points of agent 1,
name of agent 2,
points of agent 2,
memory of agent 1,
]
Returns a graph of bars comparing the average points of each agent
'''
def show_comparation(data):
        n=data[0][0]
        df=pd.DataFrame(data)

        df['agent'] = df[1]
        df['points'] = df[2]

        df = df[['agent', 'points']]
        
        average = round(df.groupby(['agent'])['points'].mean().sort_values(), 2)
        plt.title(f"Average points for {n} iteractions")
        plt.barh(average.index, average.values)
        plt.show()

'''
Recieve a list(1) of list(2) and an optional parameter where the list 2 is like:
[
number of iteractions,
name of agent 1,
points of agent 1,
name of agent 2,
points of agent 2,
memory of agent 1,
],
the optional parameter can be empty which returns a line for each agent on a number n
wich returns the top n agents ordered by points
Returns a graph of lines comparing the evolution of the average points of each agent
over several number of iteractions
'''
def show_evolution(data, *args):
    df=pd.DataFrame(data)

    df['num_iteractions'] = df[0]
    df['agent_1'] = df[1]
    df['points_1'] = df[2]

    df = df[['num_iteractions','agent_1', 'points_1']]

    averages = round(df.groupby(['agent_1','num_iteractions'])['points_1'].mean().reset_index(), 2)
    averages = averages.rename(columns={'points_1':'average'})

    if len(args)==0:
        list_agents = averages['agent_1'].unique()
    else:
         list_agents = averages.sort_values('average', ascending=False)['agent_1'].unique()[:args[0]]

    for agent in list_agents:
        df_agent = averages[averages['agent_1']==agent]
        plt.plot(df_agent['num_iteractions'], df_agent['average'], label=agent)
    
    plt.xlabel("Num-Iteractions")
    plt.ylabel("Averages")
    plt.title('Evolution with number of iteractions')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def save_csv(data, name):
    with open(f"data/{name}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)