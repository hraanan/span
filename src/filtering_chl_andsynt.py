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
in_file=open('f:/span/full_list_of_microenvironments_align_all_no_ADE_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','r')
out_file=open('f:/span/full_list_of_microenvironments_align_all_no_ADE_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4_chl_synt_filterd.txt','w')

chl_ratio_list=[]
chl_file=open('aa_content_chl_microen.txt','r')
out_file.write(in_file.readline())

non_synt_file=open('f:/span/pdb_metadata_no_synthetic.txt','r')
pdb_list=[]
for line in non_synt_file:
    line=line.split('\t')
    if line[0] not in pdb_list:
        pdb_list.append(line[0])

for line in chl_file:
    line=line.split('\t')
    if (float(line[1])/float(line[2]))>10:
        chl_ratio_list.append('_'.join(line[0].split('_')[:3]))
chl_list=[]
for line in in_file:
    line=line.split('\t')
    prot=line[0].split('.')[0]
    cof=line[0].split('.')[1].split('_')[0]
    if prot in pdb_list:
        if cof.upper() in chl:
            if line[0] in chl_ratio_list:
                out_file.write('\t'.join(line))
            
        else:
            out_file.write('\t'.join(line))
  

out_file.close()
print('end')