import igraph as ig
import networkx as nx
import numpy as np
import operator
import osmnx as ox
import pickle

ox.config(use_cache=True, log_console=True)
weight = 'length'


def make_igraph(country_name, network_type, filepath):


    # create networkx graph
    G_nx = ox.graph_from_place(country_name, network_type='all', simplify=True)
    G_nx = nx.relabel.convert_node_labels_to_integers(G_nx)

    print("Converting downloaded roads graph to igraph")
    # convert networkx graph to igraph
    G_ig = ig.Graph(directed=True)

    G_ig.add_vertices(list(G_nx.nodes()))
    G_ig.add_edges(list(G_nx.edges()))

    G_ig.vs['osmid'] = list(nx.get_node_attributes(G_nx, 'osmid').values())
    G_ig.vs['x'] = list(nx.get_node_attributes(G_nx, 'x').values())
    G_ig.vs['y'] = list(nx.get_node_attributes(G_nx, 'y').values())

    G_ig.es['length'] = list(nx.get_edge_attributes(G_nx, 'length').values())
    G_ig.es['weight'] = list(nx.get_edge_attributes(G_nx, 'length').values())
    G_ig.es['oneway'] = list(nx.get_edge_attributes(G_nx, 'oneway').values())
    G_ig.es['highway'] = list(nx.get_edge_attributes(G_nx, 'highway').values())

    # Verify conversion by comparing vertex and edge count 
    # of networkx graph and newly created igraph
    G_ig_num_v = G_ig.vcount()
    G_ig_num_e = G_ig.ecount()
    assert len(G_nx.nodes()) == G_ig.vcount()
    assert len(G_nx.edges()) == G_ig.ecount()

    print("Serializing igraph")
    pickle.dump(G_ig, open(filepath, "wb"))

    return "igraph storage for " + country_name + " roads completed"