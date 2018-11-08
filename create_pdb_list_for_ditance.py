# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:34:29 2018

@author: hraanan
"""

#create list of all cofactors and list of pdb files
in_file=open('f:/new_pymol_align_11.5.18/microenvironments_list.txt','r')
#cof_list=[]
pdbs_list=[]
for line in in_file:
    #cof=line.split('_')[0].split('.')[1]
    pdb=line.split('_')[0].split('.')[0]
    #if cof not in cof_list: cof_list.append(cof)
    if pdb.lower() not in pdbs_list: pdbs_list.append(pdb)
in_file.close()
out_file=open('f:/new_pymol_align_11.5.18/pdbs_list_for_distace.txt','w')
for pdb in pdbs_list:
    out_file.write(pdb+'\n')
    
out_file.close()
in_file.close()