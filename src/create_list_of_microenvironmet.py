# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:45:19 2018

@author: hraanan
"""

in_file=open ('f:/span/align_all_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','r')
out_file=open('f:/span/ttt_full_list_of_microenvironments_from_align_all_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','w')


in_file.readline()
microenvironments=[]
for line in in_file:
    line=line.split('\t')
    if line[0] not in microenvironments:
        microenvironments.append(line[0])
        out_file.write(line[0]+'\n')
    if line[1] not in microenvironments:
        microenvironments.append(line[1])
        out_file.write(line[1]+'\n')
print(len(microenvironments))    