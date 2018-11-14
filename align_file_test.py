# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:00:46 2018

@author: hraanan
"""
import networkx as nx

G=nx.Graph()
'''

in_file=open ('f:/new_pymol_align_11.5.18/align_1.4.txt','r')
out_file=open('f:/new_pymol_align_11.5.18/align_1.4_test.txt','w')
#out_file.write(in_file.readline())
for line in in_file:
    
    line=line.split('\t')
    out_file.write('\t'.join([line[0],line[1],line[16][:-1]])+'\n')
out_file.close()
'''
#print('end reading file')
in_file=open('f:/new_pymol_align_11.5.18/align_1.4_test.csv','r')
i=0
for line in in_file:
    #print(line)
    line=line.split('\t')
    i=i+1
    G.add_edge(line[0],line[1],whight=line[2][:-1])
    if i==10000:
        i=0
        print(G.number_of_nodes())    
in_file.close()

#'''