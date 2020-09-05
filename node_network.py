from node2vec import Node2Vec
import networkx as nx
import umap
import matplotlib.pyplot as plt

### Retrieving .GML file
G = nx.read_gml('stack_overflow_net.gml')

node_vectors = Node2Vec(G, dimensions=64, walk_length=40, num_walks=64, workers=4)
node_model = node_vectors.fit(window=10, min_count=1)
node_model.wv.most_similar('html')
node_model.wv.most_similar('python')
node_model.wv.most_similar('excel')
node_model.wv.most_similar('javascript')
node_model.wv.most_similar('git')

umap_embedding = umap.UMAP(n_neighbors=50, min_dist=0.0,
                           n_components=2, random_state=42,
                           metric='cosine').fit_transform(node_model.wv.vectors)

plt.figure(figsize=(10,9))
plt.scatter(umap_embedding[:, 0],
            umap_embedding[:, 1],
            s=3, cmap='Spectral')
