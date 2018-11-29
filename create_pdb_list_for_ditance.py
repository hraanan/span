# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:34:29 2018

@author: hraanan
"""

#create list of all cofactors and list of pdb files
in_file=open('microenvironments_metadata_chl_filterd.txt','r')
cof_list=[]
pdbs_list=[]
for line in in_file:
    cof=line.split('_')[0].split('.')[1]
    pdb=line.split('_')[0].split('.')[0]
    if cof not in cof_list: cof_list.append(cof)
    if pdb.lower() not in pdbs_list: pdbs_list.append(pdb)
in_file.close()
out_file=open('pdbs_list_for_distace.txt','w')
for pdb in pdbs_list:
    out_file.write(pdb+'\n')
    
out_file.close()
out_file=open('cofactor_list.txt','w')
for cof in cof_list:
    out_file.write(cof+'\n')
    
out_file.close()
in_file.close()