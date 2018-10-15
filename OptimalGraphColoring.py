'''
Backtracking algorithm for finding all optimal colorings of a NetworkX graph G.
'''

import networkx as nx
import grinpy as gp
from collections import OrderedDict

G = None
colorings = []

def optimal_colorings(graph):
    '''
    Takes a NetworkX graph G, outputs a list of ordered dictionaries that are optimal colorings of graph G.
    Employs a recursive backtracking algorithm.
    Each coloring will be in the form: {node1: color1, node2: color2, ...}

    User should call optimal_colorings(G). backtrack_color() and legal_color are for use within optimal_colorings(G).
    '''
    
    global colorings
    global G
    
    G = graph
    backtrack_color(G)
    
    return colorings

def backtrack_color(G, coloring = None, level = 1, chro_num = None):
    '''
    Backtracking algorithm.
    G is a NetworkX graph, coloring is an ordered dictionary, level is an integer count of the recursive depth, 
    and chro_num is the chromatic number of graph G.
    '''
    
    global colorings
    
    #If this is the first call, set up the things:
    if level == 1:
        
        #Setting up results list:
        colorings = []
        
        #Setting up coloring dictionary:
        coloring = OrderedDict()
        
        #Populating coloring dictionary:
        index = 0
        for node in G:
            
            #Color first node with color 0
            if index == 0:
                coloring[node] = 0
                index += 1
            
            #Color other nodes with nothing
            else:
                coloring[node] = None
        
        #Finding chromatic number of graph G, for future recursive calls
        chro_num = gp.chromatic_number(G)
        
        #Move to node 2
        level += 1
    
    #For all nodes in the graph:
    #for node in G.nodes: ###
    
    node_list = list(G.nodes)
        
    #For all valid colors:
    for color in range(0, chro_num):
        
        #DEBUG
        #print("checking " + str(color))

        #If the node has no neighbors with the color, color it and continue:
        if legal_color(node_list[level-1], color, coloring):
            
            #DEBUG
            #print("coloring " + str(node_list[level-1]) + " " + str(color))

            coloring[node_list[level-1]] = color

            #If not all nodes have been colored, increment level and recurse:
            if level < G.number_of_nodes():

                backtrack_color(G, coloring, (level+1), chro_num)

            #If all nodes have been colored, we have reached an optimal solution
            #(optimal since we only permitted colors up to the chromatic number)
            else:

                #Add the solution to the list
                colorings.append(coloring)
                

def legal_color(node, color, coloring):
    
    is_legal = True
    
    #Iterates through neighbors of a node
    for neighbor in G.neighbors(node):
        
        #If a neighbor already has the color being tested, the color is not legal
        if coloring[neighbor] == color:
            
            is_legal = False
            break
            
    return is_legal