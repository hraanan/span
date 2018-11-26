# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:00:46 2018

@author: hraanan
"""
import networkx as nx

G=nx.Graph()


in_file=open ('align_ca_25_rmsd_5_ratio_0.1_md_4.txt','r')
group_file=open('group101.txt','r')
nonredundant_file=open('f:/programs/span/data/cullpdb_pc90_res3.0_R0.3_d181024_chains_90%_10.24.18.txt','r')

out_align_file=open('group101_diff_cof.txt','w')
out_align_file.write(in_file.readline())

#nonredundant_file.readline()
#nonredundant=[]
#for line in nonredundant_file:
#    line=line.split('\t')
#    nonredundant.append(line[0].lower()) #+'_'+line[1])

microen_list=[]
for line in group_file:
    line=line.split('\t')
    microen_list.append(line[0])
#    #print(prot_chain)
#    if prot_chain in nonredundant:
#        #print(i)
#        non_list.append(line[0])

for line in in_file:
    line=line.split('\t')
    if line[0] in microen_list and line[1] in microen_list:
        cofs=line[4].split('_')
        if cofs[0]!=cofs[1]:
            out_align_file.write('\t'.join(line))     
#out_align_file.write('\t'.join(line))        
out_align_file.close()

#


'''

group4=[]
for line in group_file:
    line=line.split('\t')
    group4.append(line[0])
    
for line in nonre_file:
    
    out_file.write('\t'.join([line[0],line[1],line[16][:-1]])+'\n')
out_file.close()




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

'''