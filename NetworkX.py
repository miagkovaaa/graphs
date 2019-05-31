import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

G = nx.Graph()
#G = nx.random_geometric_graph(7, 1)
#G.add_edges_from([('a','d'),('b','c'),('c','d'),('b','f'),('e','c'),('d','e'),('j','e'),('j','c')])
G.add_edges_from([('a','b'),('b','c'),('c','d'),('c','f'),('e','c'),('d','f'),('f','e'),('j','c'),('j','b'),('d','e'),('b','d')])
print("Numbers of nodes:", G.number_of_nodes())
print("Nodes:", list(G.nodes))
print("Numbers of edges:", G.number_of_edges())
print("Edges:", list(G.edges))
print("The edge connectivity:", nx.edge_connectivity(G, s=None, t=None, flow_func=None, cutoff=None))
degree = []
for node in G.nodes:
    degree.append(len(list(G.adj[node])))
    #print(node,'-',G.degree[node])
degree.sort()
print("Degree of graph:", degree)
clique = list(nx.find_cliques(G))
print("Maximal cliques:", clique)
cycle = list(nx.cycle_basis(G))
print("Basis of cycles:", cycle)
T = nx.minimum_spanning_tree(G)
sorted(T.edges(data=True))


def cycling(cycle):
    C = nx.Graph()
    for cyc in cycle:
        for n in cyc:
            for i in cyc:
                if n!=i:
                    C.add_edge(n,i)

    return C.edges

M = G.number_of_edges()
"""def calculate_alpha(cycle):
    C = nx.Graph()
    for cyc in cycle:
        m = len(cyc)
        for n in cyc:
            for l in cyc:
                if n!=l:
                  edge_alphas=(for i in range(M))
    return M #C.edges"""



pos = nx.spring_layout(G)

nx.draw(G,
        pos,
        with_labels=True,
        font_weight='bold',
        font_color='white')
plt.show()

nx.draw(G,
        pos,
        edgelist=T.edges,
        width=4, edge_color='g',
        with_labels=True,
        font_weight='bold',
        font_color='white')
nx.draw(G,
        pos,
        edgelist=cycling(cycle),
        width=10, alpha=0.35, edge_color='b',
        with_labels=True,
        font_weight='bold',
        font_color='white')
plt.show()


def alpha(cyc):
    C = nx.Graph()
    for n in cyc:
        for i in cyc:
            if n != i:
                C.add_edge(n, i)
    return C.edges


for cl in clique:
    m = len(cl)
    edges = nx.draw(G, pos, edgelist=alpha(cl),
                    alpha=m / 10,
                    width=m, edge_color='#675C5C',
                    with_labels=True,
                    font_weight='bold',
                    font_color='white')
plt.show()



