# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:15:12 2020

@author: simon
"""

#open openings.dat file


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

#figure out how to find the "child" nodes and add them to a second/third/etc. columns, do some sort of regex match?
#look at current row, if any other matching the first x characters in the same position, it's a child

#use this dataframe of parent/child relationships to generate some sort of tree visualization
#maybe try a python package for the viz
#or rexport to .csv and do the viz in R
#if we do it in R, all this python code could go in an Rmarkdown code block maybe

