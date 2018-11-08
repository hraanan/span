# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:56:22 2018

@author: hraanan
"""

in_file=open ('f:/new_pymol_align_11.5.18/align_1.4.txt','r')
out_file=open('f:/new_pymol_align_11.5.18/tgroups_1.4.txt','w')
from networkx.algorithms import community
import networkx as nx
import networkx as nx

G=nx.Graph()
cofactors={}

in_file.readline()


microen_file=open('f:/new_pymol_align_11.5.18/microenvironments_list.txt','r')
microen_list=[]

for line in microen_file:
    if line[:-1] not in microen_list:
        microen_list.append(line[:-1])
microen_file.close()


for line in in_file:
    line=line.split('\t')
    if line[0] not in microen_list or line[1] not in microen_list:
        continue
    G.add_edge(line[0],line[1],whight=line[16])
print(G.number_of_nodes())    

nx.transitivity(G)    
components = [comp for comp in nx.connected_components(G)]
x=0
for comp in components:
    for node in list(comp):
        out_file.write(node+'\t'+str(x)+'\n')
    x=x+1

print('end')

out_file.close()