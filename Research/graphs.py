import networkx as nx
import sys
sys.path.append('path/to/containing/directory')
from graph_visualization import visualize
from itertools import combinations
import math

# how to merge two graphs:
'''
# Create two graphs
G1 = nx.Graph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_edges_from([('c', 'd'), ('d', 'e')])

# Merge the graphs
G_merged = nx.compose(G1, G2)
'''
#how to merge multiple graphs
'''
# Create multiple graphs
G1 = nx.Graph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])

G2 = nx.Graph()
G2.add_edges_from([('c', 'd'), ('d', 'e')])

G3 = nx.Graph()
G3.add_edges_from([('e', 'f'), ('f', 'g')])

# Merge the graphs
G_merged = nx.compose_all([G1, G2, G3])
'''

def inspect(G):
    nodes = list(G.nodes)
    edges = list(G.edges)
    
    Ginfo = {
        "Nodes": nodes,
        "Edges": edges
    }
    
    return Ginfo

def build(vertices, edges):
    """
    Create a graph using NetworkX from a list of vertices and edges.
    build([u,v,w,...], [(u, v), (w, v), ...])
    """
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    return G

def merge(*graphs):
    """
    Merge multiple NetworkX graphs into a single graph.
    """
    G = nx.Graph()
    
    for graph in graphs:
        G.add_nodes_from(graph.nodes())
        G.add_edges_from(graph.edges())
    
    return G

def path(cycle):

    C = list(cycle)
    G = nx.Graph()
    G.add_nodes_from(C)
    for i in range(len(C) - 1):
        G.add_edge(C[i], C[i + 1])
    return G

def cycle(cycle):

    C = list(cycle)
    G = nx.Graph()
    G.add_nodes_from(C)
    for i in range(len(C)):
        G.add_edge(C[i], C[(i + 1) % len(C)])
    return G

def star(hub, neighbors):

    leaves = list(neighbors)
    G = nx.Graph()
    G.add_node(hub)
    for node in leaves:
        G.add_node(node)
        G.add_edge(hub, node)
    return G

def trees(n):
    def is_isomorphic_to_any(graph, graph_list):
        for g in graph_list:
            if nx.is_isomorphic(graph, g):
                return True
        return False

    all_trees = []
    nodes = list(range(n + 1))  # A tree with n edges has n+1 nodes

    for edges in combinations(combinations(nodes, 2), n):
        G = nx.Graph()
        G.add_edges_from(edges)
        if nx.is_tree(G) and not is_isomorphic_to_any(G, all_trees):
            all_trees.append(G)

    return all_trees
#notebook

#8 ( mod 14)

#(61)-1
G1  = merge(path([20,11,1,math.inf, 0, 9, 19]), path([2,10]))
G2 = merge(path([5,13,2,math.inf, 3, 11, 0]), path([19,8]))
G3 = merge(path([3,12,4,math.inf, 5, 14, 1]), path([19,8]))
G4 = merge(path([3,13,0,10, 1, 9, 18]), path([math.inf,6]))
G5 = merge(path([0,6,1,5, 2, 9, 7]), path([3,4]))

F_61_1 = [G1,G2,G3,G4,G5] #defines the decomposition 'object' a list of graph labelings
#visualize(F_61_1, '(61)-1', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#(61)-2
G1  = merge(path([9,0,math.inf,1,11,20]),path([1,13]), path([2,12]))
G2  = merge(path([13,2,math.inf,3,11,0]),path([3,16]), path([12,20]))
G3  = merge(path([3,12,4,math.inf,5,14]),path([math.inf,6]), path([0,8]))
G4  = merge(path([13,0,10,1,9,18]),path([1,12]), path([6,17]))
G5  = merge(path([0,6,1,5,2,9]),path([5,3]), path([7,8]))

F_61_2 = [G1,G2,G3,G4,G5]
#visualize(F_61_2, '(61)-2', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#(61)-3
G1 = merge(path([11,1,math.inf,0,9,17]),path([9,19]), path([4,13]))
G2  = merge(path([11,3,math.inf,2,13,5]),path([1,13]), path([7,18]))
G3  = merge(path([14,5,math.inf,4,12,3]),path([1,12]), path([7,15]))
G4  = merge(path([9,1,10,0,13,3]),path([13,math.inf]), path([2,11]))
G5  = merge(path([0,6,1,5,2,9]),path([2,4]), path([7,8]))

F_61_3 = [G1,G2,G3,G4,G5]
#visualize(F_61_3, '(61)-3', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#(61)-4
G1 = merge(star(1,[14,11,13,math.inf]),path([20,7,math.inf]), path([8,19]))
G2 = merge(star(3,[13,math.inf,16,11]),path([9,0,11]), path([6,19]))
G3 = merge(star(math.inf,[2,5,6,4]),path([3,12,4]), path([7,19]))
G4 = merge(star(9,[20,18,19,1]),path([0,10,1]), path([4,13]))
G5 = merge(star(1,[5,6,7,4]),path([9,2,4]), path([11,10]))

F_61_4 = [G1,G2,G3,G4,G5]
#visualize(F_61_4, '(61)-4', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#(61)-5
G1 = merge(path([7,math.inf,1,13,0]),path([14,1,11]), path([8,19]))
G2 = merge(path([0,11,3,16,7]),path([13,3,math.inf]), path([6,19]))
G3 = merge(path([12,4,math.inf,5,17]),path([2,math.inf,6]), path([7,19]))
G4 = merge(path([10,1,9,18,6]),path([20,9,19]), path([7,17]))
G5 = merge(path([3,8,1,4,2]),path([5,1,7]), path([9,10]))

F_61_5 = [G1,G2,G3,G4,G5]
#visualize(F_61_5, '(61)-5', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')

#(61)-6
G1 = merge(star(7,[20,15,math.inf]),star(1,[math.inf,13,11]),path([8,19]))
G2 = merge(star(0,[9,12,11]),star(3,[11,16,math.inf]),path([4,13]))
G3 = merge(star(12,[20,3,4]),star(math.inf,[4,6,5]),path([2,13]))
G4 = merge(star(12,[20,3,4]),star(math.inf,[4,6,5]),path([2,13]))
G3 = merge(star(12,[20,3,4]),star(math.inf,[4,6,5]),path([2,13]))

F_61_6 = [G1,G2,G3,G4,G5]
visualize(F_61_6, '(61)-6', 'C:\\Users\\baneg\\OneDrive\\Desktop\\Git\\Python\\Research\\8 (mod 14)\\texgraph')
