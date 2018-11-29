# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:10:08 2018

@author: hraanan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:35:48 2017

@author: hraanan
"""
    
chl=['BCB','BCL','CHL','CL0','CLA','PHO','PMR','BPB','BPH']
#out_file=open('seq.txt','w')
in_file=open('full_microenvironments_list_align_ca_25_rmsd_5_ratio_0.1_md_2.txt','r')
out_file=open('full_microenvironments_list_align_ca_25_rmsd_5_ratio_0.1_md_2_synt_chl_filterd.txt','w')

chl_ratio_list=[]
chl_file=open('chl_aa_ratio.txt','r')
out_file.write(in_file.readline())

non_synt_file=open('pdb_metadata_no_synthetic.txt','r')
pdb_list=[]
for line in non_synt_file:
    line=line.split('\t')
    if line[0] not in pdb_list:
        pdb_list.append(line[0])

for line in chl_file:
    line=line.split('\t')
    if float(line[3])>10:
        chl_ratio_list.append(line[0])
chl_list=[]
for line in in_file:
    line=line.split('\t')
    prot=line[0].split('.')[0]
    cof=line[0].split('.')[1].split('_')[0]
    
    if prot in pdb_list:
        
        if cof.upper() in chl:
            if line[0][:-1] in chl_ratio_list:
                out_file.write('\t'.join(line))
            
        else:
            out_file.write('\t'.join(line))
  

out_file.close()
print('end')