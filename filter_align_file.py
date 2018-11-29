# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:09:20 2018

@author: hraanan
"""

import sys

in_flie_name=sys.argv[1]
in_file=open(in_flie_name,'r')
out_file=open('out_'+in_flie_name,'w')
ratio=.1
ca=25
md=4
rmsd=5
in_file.readline()
x=0 
y=0  

for line in in_file:
    x=x+1    
    line=line.split('\t')
    
    try:
       if float(line[11])<ratio and float(line[5])<rmsd and float(line[6])>ca and float(line[9])<md:
                y=y+1
                join_line= '\t'.join(line)  
                out_file.write(join_line)
    except:# IndexError:
        print('err')        
        continue
print(y,x)
print('end')
out_file.close()