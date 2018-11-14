# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:56:22 2018

@author: hraanan
"""
in_file=open ('f:/new_pymol_align_11.5.18/align_1.3.txt','r')
out_file=open('f:/new_pymol_align_11.5.18/groups_1.3.txt','w')
from networkx.algorithms import community
import networkx as nx


G=nx.Graph()
cofactors={}

in_file.readline()


microen_file=open('f:/new_pymol_align_11.5.18/microenvironments_list_1.3.txt','r')
microen_list=[]

for line in microen_file:
    #line=line.split('\t')
    #if line[:-1] not in microen_list:
    microen_list.append(line[:-1])
microen_file.close()
print(len(microen_list))
i=0
for line in in_file:
    line=line.split('\t')
    #if line[0] in microen_list or line[1] in microen_list:
    G.add_edge(line[0],line[1],whight=line[16][:-1])
    i=i+1
    #if i==50000:
     #   i=0
       # break
      #  print(G.number_of_nodes())    
print('total nodes:',G.number_of_nodes())    

for node in G.nodes():
    if node not in microen_list:
        G.remove_node(node)
#for microen in microen_list:
#    if G.has_node(microen)==False:
#        G.remove_node(microen)
print('filterd nodes:',G.number_of_nodes())  
nx.write_gexf(G, 'f:/new_pymol_align_11.5.18/full_graph.gexf')

nx.transitivity(G)    
components = [comp for comp in nx.connected_components(G)]
x=0
for comp in components:
    for node in list(comp):
        out_file.write(node+'\t'+str(x)+'\n')
    x=x+1

print('end')

out_file.close()