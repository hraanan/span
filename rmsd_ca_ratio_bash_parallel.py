# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:28:30 2018

@author: hraanan
"""
import sys
in_file_name=sys.argv[1]
print(in_file_name)
out_file=open(in_file_name+'_out.txt','w')

in_file=open(in_file_name,'r')   
#in_file=open('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all.txt',"r")

#out_file=open('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_rmsd_ca__md_only.txt',"w")
#out_file.write('source\ttarget\trmsd\tca\trmsd\ca\tmd\n')
#in_file.readline()
for line in in_file:
  
        line=line.split("\t")
        try:
            out_file.write('\t'.join(line)[:-1]+'\t'+str(float(line[5])/float(line[6]))+'\n')
        except:# ZeroDivisionError:
            continue
            

print('end')