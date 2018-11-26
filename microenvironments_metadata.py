# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:56:22 2018

@author: hraanan
"""

in_file=open ('groups_align_ca_25_rmsd_5_ratio_0.1_md_4.txt','r')
out_file=open('microenvironments_metadata.txt','w')
pdb_file=open('pdbs_metadata.txt','r')
cof_file=open('F:\programs\span\data\manual_cofactor_atoms_list.txt','r')
microen_list=[]
fes=['SF4','FES','F3S']

pdb_dict={}
for line in pdb_file:
    line=line.split('\t')
    if line[0] not in pdb_dict.keys():
        pdb_dict[line[0]]=line[2:]
pdb_file.close()
cof_dict={}

for line in cof_file:
    line=line.split('\t')
    if line[1] not in cof_dict:
        cof_dict[line[1]]=line[2]
cof_file.close()

for line in in_file:
    line=line[:-1]
    line=line.split('\t')
    cof=line[0].split('.')[1].split('_')[0]
    if cof in cof_dict:
        cof_type=cof_dict.get(cof)
    elif cof in fes:
        cof_type='fes'
    else:
        cof_type='other'
        
    metadata=pdb_dict.get(line[0].split('.')[0])
    out_file.write('\t'.join(line)+'\t'+cof+'\t'+cof_type+'\t'+'\t'.join(metadata))

print('end')

out_file.close()
