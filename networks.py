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
    sof = nx.Graph()

