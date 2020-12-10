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

#coding todo draft:

#open openings.dat file
from pathlib import Path
filename = Path("data/openings.dat")
with open(filename.absolute()) as myfile:
    head = [next(myfile) for x in range(3)]
print(head)

#concatonate top 3 lines with underscore delimiter and "df_openingsdat_" at front
#store this in a variable to use as the name of a dataframe we create later, or just create an empty dataframe right now
#e.g.
# 7
# 12643
# 600
#...becomes:
# df_openingsdat_7_12643_600

#delete top 3 lines

#for all odd lines, add to the end of the line, concatonate space + the line below them
#e.g.
# N07 N26 G S10 S35 G
# S39
#...becomes:
# N07 N26 G S10 S35 G S39

#delete all even lines

#add the remain lines (all the odd lines) to the dataframe in the first column called nodes
#trim all the lines so there is no whitespace on either side

#figure out how to find the "child" nodes and add them to a second/third/etc. columns, do some sort of regex match?
#look at current row, if any other matching the first x characters in the same position, it's a child

#idea: add a column with the length of each string. if the length is less than the current row, then try to match that many characters

#use this dataframe of parent/child relationships to generate some sort of tree visualization
#maybe try a python package for the viz like this one:
    #https://pyvis.readthedocs.io/en/latest/tutorial.html
#or rexport to .csv and do the viz in R
#if we do it in R, all this python code could go in an Rmarkdown code block maybe

#maybe when doing the viz, only include nodes that have parent-child relationships, so it doesn't get too large
#show a count of nodes without parent-child relationships to get an idea of what they're useful for