# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:09:20 2018

@author: hraanan
"""

in_file=open ('align_ca_25_rmsd_5_ratio_0.1_md_2.txt','r')
out_file=open('full_microenvironments_list_align_ca_25_rmsd_5_ratio_0.1_md_2.txt','w')
import networkx as nx

G=nx.Graph()
cofactors={}

in_file.readline()

for line in in_file:
    line=line.split('\t')
    G.add_edge(line[0],line[1],whight=line[11][:-1])
print(G.number_of_nodes())
for node in G.nodes():
    out_file.write(node+'\n')
out_file.close()