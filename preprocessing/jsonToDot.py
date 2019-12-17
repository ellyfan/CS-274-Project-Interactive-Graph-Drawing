import pandas as pd
import networkx as nx
import json
import seaborn as sns

mis_file = open('miserables.json')
les_mis_json = json.load(mis_file)
mis_links = pd.DataFrame(les_mis_json['links'])
mis_nodes = pd.DataFrame(les_mis_json['nodes'])

edge_list_df = pd.merge(mis_links,mis_nodes,left_on='source',right_index=True)
edge_list_df = pd.merge(edge_list_df,mis_nodes,left_on='target',right_index=True,suffixes=('_source','_target'))

edge_list_df.drop(['group_source','group_target','source','target'],axis=1,inplace=True)

le_graph = nx.from_pandas_edgelist(edge_list_df,'name_source','name_target')

nx.write_graphml(le_graph,'miserables.graphml')