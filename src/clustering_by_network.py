# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:44:04 2018

@author: hraanan
"""

in_file=open ('f:/span/align_all_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','r')
out_file=open('f:/span/groups_align_all_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','w')
#import community
from networkx.algorithms import community
import networkx as nx

G=nx.Graph()
cofactors={}

in_file.readline()

for line in in_file:
    line=line.split('\t')
    G.add_edge(line[0],line[1],whight=line[19])
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