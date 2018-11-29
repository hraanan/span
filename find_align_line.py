# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:09:20 2018

@author: hraanan
"""

import sys

in_flie_name=sys.argv[1]
in_file=open(in_flie_name,'r')

for line in in_file:
    line=line.split('\t')
    if line[0]=='2vzb.FE_B_6204' and line[1]=='1x9f.HEM_C_160':
        out_file=open('out_file.txt','w')
        out_file.write(in_flie_name)
        out_file.write('\t'.join(line))
        break