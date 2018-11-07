# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:01:28 2018

This creates a list for pairwise alignment 


@author: hraanan
"""
import os
import time
from multiprocessing import Pool

rootdir ='F:/microfolds_8_2018/all/' # folder of the pdb original filesdownladed form the pdb
out_file=open('align_cofactors.txt','w')


def cof_align_list(path):
    files_list=os.listdir(path)
    align_list=[]
    cof=path.split('/')[3]
    temp_file=open(cof+'_align.txt','w')
    for i,f_i in enumerate(files_list):
        for j,f_j in enumerate(files_list):
            if j>i:
                
                temp_file.write(f_i+'\t'+f_j+'\n')
    temp_file.close()
    return cof+'_align.txt'
        

if __name__ == '__main__':

    dir_list=[]
    for subdir, dirs, files in os.walk(rootdir):
        dir_list.append(subdir)
    with Pool(8) as p:
        for temp_file in p.imap_unordered(cof_align_list, dir_list[1:]):
            print(temp_file)
            #tempfile=open(temp_file,'r')
            #out_file.write(tempfile.read())
            #tempfile.close()
                
out_file.close()
print('end')
        
        