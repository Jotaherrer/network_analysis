import networkx as nx
import pandas as pd


def get_data(csv_file):
    '''
    Extracts data from .CSV files related with nodes and edges
    '''
    data = pd.read_csv(csv_file)
    return data


if __name__ == '__main__':
    edges_data = get_data('stack_network_links.csv')
    nodes_data = get_data('stack_network_nodes.csv')
    edges_data.head()
    nodes_data.head()

    ### Building network
    G = nx.Graph()

    for index, info in nodes_data.iterrows():
        G.add_node(info['name'], group=info['group'], nodesize=info['nodesize'])

    for index, info in edges_data.iterrows():
        G.add_edge(info['source'], info['target'], weight=info['value'])

    G.nodes
    G.edges
    G.number_of_nodes()
    G.number_of_edges()
    G.nodes['html']
    G.nodes['python']
    G.nodes['javascript']
    G.degree()

    # Average path length
    nx.average_shortest_path_length(G)