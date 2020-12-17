# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:15:12 2020

@author: simon
"""

################################################################################
#
####    What is the purpose of this script?
#           Help us understand what's in the opening book by:
#           1. open openings.dat
#           2. transform it into a hierarchy of nodes
#           3. visualize it (or pass it to another tool for visualization via .csv export)
#
####    What do the first 3 lines of openings.dat mean?
#           7     #the number of turns deep the opening book has been calculated for
#           12643 #not sure, probably a count of the number of simulations that were run
#           600   #number of seconds the AI got to think for each turn
#
####    What do the lines after the first 3 lines of openings.dat mean?
#           N07 N26 G S10 S35 G   #the game history so far
#           S39                   #the next-best-move, given the above game history line
#           # then it repeats
#           #    game history line
#           #    followed by next-best-move
#           #        always in pairs
#       Note: The code that generated openings.dat is here:
#             https://github.com/skotz/volcanoes/blob/master/Volcanoes/Engine/OpeningBook.cs#L156
#
####    How do we turn openings.dat into a hierarchy of nodes?
#           1. simplify the pairs of lines into one line. this:
#                  N07 N26 G S10 S35 G
#                  S39
#              ...becomes this:
#                  N07 N26 G S10 S35 G S39
#              ...which is what the game transcript will look like after the best move is taken anyway
#           2. find lines which happened earlier in the same game and make them parents to the later child-lines. e.g.
#               N07 N26 G S10 S35        #this line
#               N07 N26 G S10 S35 G S39  #...would be parent to this line
#
################################################################################

#import packages
from pathlib import Path
import pandas as pd
import numpy as np

#open openings.dat file and convert each line into an item in a list
filename = Path("data/openings.dat")
with open(filename.absolute()) as myfile:
    openings_list = list(myfile)

#remove linebreaks
for i in range(len(openings_list)):
    item = openings_list[i]
    openings_list[i] = item.strip()

#remove first 3 items
_, _, _, *openings_list = openings_list

#concatonate pairs of items with a space between them
#e.g.
# N07 N26 G S10 S35 G
# S39
#...becomes:
# N07 N26 G S10 S35 G S39
openings_list = [openings_list[i] + " " + openings_list[i+1] for i in range(0, len(openings_list)-1, 2)]

#create dataframe from openings_list as column called "node"
df = pd.DataFrame (openings_list,columns=["node"])

#remove spaces from beginning and end of node cells
df["node"] = df["node"].str.strip()

#create column called count_of_spaces_in_node
def countSpaces(cell):
    try:
        return cell.count(" ")
    except:
        return 0
df["count_of_spaces_in_node"] = df["node"].apply(countSpaces)

#sort by count_of_spaces_in_node, then by node
df = df.sort_values(by=["count_of_spaces_in_node", "node"])

#reset index
df = df.reset_index(drop=True)

#what are the unique values in count_of_spaces_in_node?
hierarchy_distinct_count_of_spaces_in_node = df.count_of_spaces_in_node.unique()

#create column called length_of_node
df['length_of_node']  = df['node'].str.len()


#create parent_node column
#( thanks to help from Saravanakumar V here: https://stackoverflow.com/a/65334898/279659 )
node_list = [i.split() for i in df["node"]]
def findParentNode(x):
    lis = x.split(" ")
    for i in range(-1,-len(lis),-1):
        if (lis[:i] in node_list):
            return " ".join(lis[:i])
    return np.nan
df["parent_node"] = df["node"].apply(findParentNode)

#now get the data into .csv format for viz in R
#create a df ready to use as nodes.csv



#save df_nodes to csv
# df_nodes.to_csv(r'data/nodes.csv', index = False)

#idea: remove nodes without parent nodes, but consider replacing them with one node showing how many nodes don't have parent nodes



#create a df ready to use as edges.csv

#idea


#save df_edges to csv
# df_edges.to_csv(r'data/edges.csv', index = False)
