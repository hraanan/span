# -*- coding: utf-8 -*-
"""


takes input file and creates two files ADE aligns and no AED aligns 

@author: hraanan
"""
import sys
in_file_name=sys.argv[1]

out_file=open(in_file_name[:-4]+'_NO_ADE.txt','w')
ade_file=open(in_file_name[:-4]+'ADE.txt','w')

head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n'
out_file.write(head)
ade_file.write(head)

#NAD=['NAD','ADJ','ENP','NAP','NDP','NJP','NZQ','XNP']

in_file=open(in_file_name,'r')   
in_file.readline()

for line in in_file:
    try:
        line=line.split('\t')
        if line[0].split('_')[0].split('.')[1]=='ADE' or line[1].split('_')[0].split('.')[1]=='ADE' :
            ade_file.write('\t'.join(line))
        else:
            out_file.write('\t'.join(line))
        

    except Exception as e:
         print (line)
         print(e)
         continue
   
out_file.close()
ade_file.close()
print(end)
#'''

