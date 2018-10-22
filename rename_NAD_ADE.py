# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:31:50 2018
takes input files: 
align_all_ligands_and_nonredundant_metal_filterd.txt
align_nonredundant_org_new_center.txt
align_organicNewCenter_all.txt
creates two files ADE aligns and no AED aligns 

@author: hraanan
"""

out_file=open('f:/span/align_all_ADE_rename_2016.txt','w')
#ade_file=open('f:/span/align_ADE_2016.txt','w')


head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n'
out_file.write(head)
#ade_file.write(head)

NAD=['NAD','ADJ','ENP','NAP','NDP','NJP','NZQ','XNP']
in_file=open('F:\span/align_nonredundant_org_new_center.txt','r')   
in_file.readline()
#l=['4yjf.FAD_B_401_oxidoreductase_1.4.3.3', '3f2y.FMN_X_200_rna_1.-.-.-', 'FAD', 'FMN', '118', '0', 'FAD_FMN', '1', '0.0', '0', '0.0', '0', '19.7139742746', '118\n']
for line in in_file:
    try:
        line=line.split('\t')
       
        if len(line[0].split('_')[3])>3:
            if line[0].split('_')[3][3]=='-':
                #print(line[0])
                line[0]=line[0].split('_')
                line[0][0]=line[0][0][:4]+'.ADE'
                line[0]='_'.join(line[0])
                #print(line[0])
        if len(line[1].split('_')[3])>3:
            if line[1].split('_')[3][3]=='-':
                #print(line[1])
                line[1]=line[1].split('_')
                line[1][0]=line[1][0][:4]+'.ADE'
                line[1]='_'.join(line[1])
                #print(line[1])
    except Exception as e:
         print (line)
         print(e)
         continue
   
    out_file.write('\t'.join(line))
in_file=open('F:\span/align_organicNewCenter_all.txt','r')

for line in in_file:
    try:
        line=line.split('\t')
         
        if len(line[0].split('_')[3])>3:
            if line[0].split('_')[3][3]=='-':
                #print(line[0])
                line[0]=line[0].split('_')
                line[0][0]=line[0][0][:4]+'.ADE'
                line[0]='_'.join(line[0])
                #print(line[0])
        if len(line[1].split('_')[3])>3:
            if line[1].split('_')[3][3]=='-':
                #print(line[1])
                line[1]=line[1].split('_')
                line[1][0]=line[1][0][:4]+'.ADE'
                line[1]='_'.join(line[1])
                #print(line[1])
    except Exception as e:
         print (line)
         print(e)
         continue
    out_file.write('\t'.join(line))

in_file=open('F:\span/align_all_ligands_and_nonredundant_metal_filterd.txt','r')
for line in in_file:
    for line in in_file:
        out_file.write('\t'.join(line))
#

#ade_file.close()
out_file.close()
#'''