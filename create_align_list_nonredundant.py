# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:01:28 2018

This creates a list for pairwise alignment 


@author: hraanan
"""
import os
import time
from multiprocessing import Pool

rootdir ='F:/microfolds_8_2018/new_all/' # folder of the pdb original filesdownladed form the pdb
out_file=open('f:/span_11.17.18/nonredundant_microenvironments.txt','w')




def in_list(file):
    if file.split('.')[0].upper() in nonredundant_pdb_list:
        return file
    else:
        return 0



nonredundant_file=open('F:/programs/span/data/cullpdb_pc90_res3.0_R0.3_d181024_chains_90%_10.24.18.txt','r')        
nonredundant_file.readline()
nonredundant_pdb_list=[]
for line in nonredundant_file:
    #line=line.split('\t')
    if line[0:4] not in nonredundant_pdb_list:
        nonredundant_pdb_list.append(line[0:4])
        
if __name__ == '__main__':
    nonredundant_file_list=[]
    file_list=[]
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_list.append(file)    
    
    with Pool(8) as p:
        for file in p.imap_unordered(in_list, file_list):
            
            if file!=0:
                nonredundant_file_list.append(file)
                out_file.write(file+'\n')
                
    out_file=open('align_nonredundant_list.txt','w')
    for i,f_i in enumerate(nonredundant_file_list):
        for j,f_j in enumerate(nonredundant_file_list):
            if j>i:
                out_file.write(f_i+'\t'+f_j+'\n')

out_file.close()
print('end')
        
        