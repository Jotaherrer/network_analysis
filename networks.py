import networkx as nx
import pandas as pd
import community as community_louvain


def get_data(csv_file):
    '''
    Extracts data from .CSV files related with nodes and edges
    '''
    data = pd.read_csv(csv_file)
    return data


def build_net(nodes_data, edges_data):
    """
    Builds network by inserting nodes and edges as determined in the dataset.
    """
    for index, info in nodes_data.iterrows():
        G.add_node(info['name'], group=info['group'], nodesize=info['nodesize'])

    for index, info in edges_data.iterrows():
        G.add_edge(info['source'], info['target'], weight=info['value'])
    return None


if __name__ == '__main__':
    edges = get_data('stack_network_links.csv')
    nodes = get_data('stack_network_nodes.csv')
    edges.head()
    nodes.head()

    ### Building network
    G = nx.Graph()
    build_net(nodes, edges)

    ### Nodes and edges review and save
    G.nodes
    G.edges
    G.number_of_nodes()
    G.number_of_edges()
    print(nx.info(G))
    G.nodes['html']
    G.nodes['python']
    G.degree()
    nx.write_gml(G,"stack_overflow_net.gml")
    
    ### Centrality metrics
    # Betweenness centrality
    bet_dict = nx.betweenness_centrality(G, weight='inv_weight')
    bet_sorted = sorted(bet_dict.items(), key=lambda x: x[1], reverse=True)
    bet_sorted[:10]
    # Closeness centrality
    close_dict = nx.closeness_centrality(G, distance="inv_weight")
    close_sorted = sorted(close_dict.items(), key=lambda x: x[1], reverse=True)
    close_sorted[:10]
    # Pagerank centrality
    pr_dict = nx.pagerank(G, weight="weight")
    pr_sorted = sorted(pr_dict.items(), key=lambda x: x[1], reverse=True)
    pr_sorted[:10]
    # Modularity
    mod_dict = community_louvain.best_partition(G, weight="weight")
    mod_sorted = sorted(mod_dict.items(), key=lambda x: x[1], reverse=True)
    # Degree centrality
    degree_centre = nx.degree_centrality(G)
    degree_sorted = sorted(degree_centre.items(), key=lambda x: x[1], reverse=True)
    degree_sorted[:10]

    ### Testing .GML file
    G = nx.read_gml("stack_overflow_net.gml")