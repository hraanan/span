# -*- coding: utf-8 -*-
"""


takes input file and creates two files ADE aligns and no AED aligns 

@author: hraanan
"""
import sys
in_file_name=sys.argv[1]
print(in_file_name)
out_file=open(in_file_name+'_NO_ADE.txt','w')
ade_file=open(in_file_name+'_ADE.txt','w')

in_file=open(in_file_name,'r')   
in_file.readline()

for line in in_file:
    #try:
        line=line.split('\t')
        if line[0].split('_')[0].split('.')[1]=='ADE' or line[1].split('_')[0].split('.')[1]=='ADE' :
            ade_file.write('\t'.join(line)[:-1]+'\t'+str(float(line[5])/float(line[6]))+'\n')
        else:
            out_file.write('\t'.join(line)[:-1]+'\t'+str(float(line[5])/float(line[6]))+'\n')
        

    #except Exception as e:
      #   print (line)
      #   print(e)
      #   continue
   
out_file.close()
ade_file.close()
print('end')
#'''

