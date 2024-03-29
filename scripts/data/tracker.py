import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

'''
Recieve a list(1) of list(2) and a list of optional parameters, where the list 2 is like:
[
number of iteractions,
name of agent 1,
points of agent 1,
name of agent 2, 
points of agent 2,
memory of agent 1,
]
if a second optional parameter is given, the graphic with be saved with 
the name of that parameter in the folder 'data/img'
Returns a graph of bars comparing the average points of each agent
if parameter show is equalized to True, the graph will be show. Otherwise it will only be saved
'''
def show_comparation(data, *args, show=False, overwrite=True):
        plt.clf()
        n=data[0][0]
        df=pd.DataFrame(data)
        name = args[0] if len(args)!=0 else None

        df['agent'] = df[1]
        df['points'] = df[2]

        df = df[['agent', 'points']]
        
        average = round(df.groupby(['agent'])['points'].mean().sort_values(), 2)
        df_average = pd.DataFrame({'agent': average.index, 'points': average.values})
        plt.title(f"Average points for {n} iteractions")
        plt.barh(df_average['agent'],df_average['points'])
        if name:
            if overwrite:
                plt.savefig(f'data/img/{name}.png',bbox_inches='tight')
            else:
                save_graph(f'{name}.png', 'data/img')
        if show:
            plt.show()

'''
Recieve a list(1) of list(2) and an list of optional parameters where the list(2) is like:
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
if a second optional parameter is given, the function will save the graphic with the name of
that parameter in the folder 'data/img'
Returns a graph of lines comparing the evolution of the average points of each agent
over several number of iteractions
if parameter show is equalized to True, the graph will be show. Otherwise it will only be saved
'''
def show_evolution(data, *args, show = False, overwrite=True):
    plt.clf()
    top = args[0] if type(args[0])==int else None
    name = args[0] if len(args)>0 and top==None else args[1]

    df=pd.DataFrame(data)

    df['num_iteractions'] = df[0]
    df['agent_1'] = df[1]
    df['points_1'] = df[2]

    df = df[['num_iteractions','agent_1', 'points_1']]

    averages = round(df.groupby(['agent_1','num_iteractions'])['points_1'].mean().reset_index(), 2)
    averages = averages.rename(columns={'points_1':'average'})

    if top:
        list_agents = averages.sort_values('average', ascending=False)['agent_1'].unique()[:top]
    else:
        list_agents = averages['agent_1'].unique()

    for agent in list_agents:
        df_agent = averages[averages['agent_1']==agent]
        plt.plot(df_agent['num_iteractions'], df_agent['average'], label=agent)
    
    plt.xlabel("Num-Iteractions")
    plt.ylabel("Averages")
    if top:
        plt.title(f'Evolution of top {top} agents with number of iteractions')
    else: 
        plt.title('Evolution with number of iteractions')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if name:
        if top:
            if overwrite:
                plt.savefig(f'data/img/{name}_top{top}.png',bbox_inches='tight')
            else:
                save_graph(f'{name}_top{top}.png', 'data/img')
        else:
            if overwrite:
                plt.savefig(f'data/img/{name}.png',bbox_inches='tight')
            else:
                save_graph(f'{name}.png', 'data/img')

    if show: 
        plt.show()

'''
Recieve an array of data and a name.
Save the array of data in the folder 'data/csv' with the name given
'''
def save_csv(data, name):
    with open(f"data/csv/{name}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def agent_optimization(data, name, save=False, show=True, overwrite=True):
        plt.clf()
        n=data[0][0]
        df=pd.DataFrame(data)

        df['agent'] = df[1]
        df['points'] = df[2]

        df = df[['agent', 'points']]
        
        average = round(df.groupby(['agent'])['points'].mean().sort_values(), 2)
        df_average = pd.DataFrame({'agent': average.index, 'points': average.values})

        print(df_average)
        print("agent name: "+ name)
        result = df_average[df_average['agent'].str.contains(name)]
        print(result)
        plt.title(f"comparation of {name} values")
        plt.barh(result['agent'], result['points'])
        if save:
            if overwrite:
                plt.savefig(f'data/img/comparation/optimization_{name}.png',bbox_inches='tight')
            else:
                save_graph(f'optimization_{name}', 'data/img/comparation')
        if show:
            plt.show()

def save_graph(name, route='', table=False):
    i = 0
    file_name = name if not table else name+'.png'
    while os.path.exists(os.path.join(route, file_name)):
        i += 1
        file_name = f"{name.replace('.png', '')}({i}).png"
    plt.savefig(os.path.join(route, file_name), bbox_inches='tight')

def show_table(data, type, show=False, overwrite=False, save=True):
    plt.clf()
    df=pd.DataFrame(data)
    df ['agent'] = df[1]
    df ['points'] = df[2]
    df ['majority'] = df[5]

    df= df[['agent', 'points', 'majority']]
    
    average= round(df.groupby(['agent', 'majority'])['points'].mean(), 2)
    aux=  pd.DataFrame({'agent': average.index.get_level_values(0),
                        'majority': average.index.get_level_values(1),
                         'points': average.values})

    df_pivot = aux.pivot(index='agent', columns='majority', values='points')

    if type=='color' or type=='color-desc':
        plt.imshow(df_pivot, cmap='viridis')

        plt.title(f'No equivalente table for {data[0][0]} interactions')
        plt.xticks(range(len(df_pivot.columns)), df_pivot.columns, rotation=90)
        plt.yticks(range(len(df_pivot.index)), df_pivot.index)

        num_rows, num_cols = df_pivot.shape
        if type=='color-desc':
            for i in range(num_rows):
                for j in range(num_cols):
                    plt.text(j, i, f'{df_pivot.iloc[i, j]:.1f}', ha='center', va='center', color='white', fontsize=8, bbox=dict(boxstyle='round', facecolor='none', edgecolor='none'))
        plt.colorbar()
        if save:
            if overwrite:
                plt.savefig(f'data/img/No_equivalent_table_{data[0][0]}_interactuions.png',bbox_inches='tight')
            else:
                save_graph(f'table_{data[0][0]}_interactuions', 'data/img', table=True)
            if show:
                plt.show()
    elif type=='numeric':
        tab = plt.table(cellText=df_pivot.values, 
                 rowLabels=df_pivot.index,
                 colLabels=df_pivot.columns, 
                 loc='center', 
                 cellLoc='center')

        plt.axis("off")
        plt.xticks(range(len(df_pivot.columns)), df_pivot.columns, rotation=90)
        tab.auto_set_font_size(False)
        tab.set_fontsize(8)
        tab.auto_set_column_width(col=list(range(len(df_pivot.columns))))
        if save:
            if overwrite:
                plt.savefig(f'data/img/No_equivalent_table_{data[0][0]}_interactuions.png',bbox_inches='tight')
            else:
                save_graph(f'table_{data[0][0]}_interactuions', 'data/img', table=True)
        if show:
            plt.show()