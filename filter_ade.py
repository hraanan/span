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


#in_file=open('F:\span/align_all_ligands_and_nonredundant_metal_filterd.txt','r')
#print(in_file.readline())
#in_file=open('F:\span/align_organicNewCenter_all.txt','r')
#print(in_file.readline())


out_file=open('f:/span/align_all_2016.txt','w')
ade_file=open('f:/span/align_ADE_2016.txt','w')


#print(in_file.readline())
head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n'
out_file.write(head)
ade_file.write(head)

NAD=['NAD','ADJ',	'ENP','NAP','NDP','NJP','NZQ','XNP']
in_file=open('F:\span/align_nonredundant_org_new_center.txt','r')   
in_file.readline()
for line in in_file:
    line=line.split('\t')
    cof1=line[0].split('_')[0]
    cof2=line[1].split('_')[0]
    cof1=cof1.split('.')[1]
    cof2=cof2.split('.')[1]
   # print(cof1,cof2)       
    if cof1=='ADE' or cof2=='ADE':
        ade_file.write('\t'.join(line))
    elif cof1 in NAD:
        if line[0].split('_')[3][3]=='-':
            
            #cof1=line[0].split('_')[3][0:3]
            line[0]=line[0].split('_')
            line[0][0]=line[0][0][:4]+'.ADE'
            line[0]='_'.join(line[0])
            #print(line[0])
            ade_file.write('\t'.join(line))
            continue
    elif cof2 in NAD:
        if line[1].split('_')[3][3]=='-':
            #print(line[1])
            line[1]=line[1].split('_')
            line[1][0]=line[1][0][:4]+'.ADE'
            line[1]='_'.join(line[1][:3])
            #print(line[1])
            ade_file.write('\t'.join(line))
            continue
    out_file.write('\t'.join(line))
in_file=open('F:\span/align_organicNewCenter_all.txt','r')
for line in in_file:
    line=line.split('\t')
    cof1=line[0][5:8]
    cof2=line[1][5:8]
   # print(cof1,cof2)       
    if cof1=='ADE' or cof2=='ADE':
        line[0]='_'.join(line[0].split('_')[:3])
        line[1]='_'.join(line[1].split('_')[:3])
        ade_file.write('\t'.join(line))
    elif cof1 in NAD:
        if line[0].split('_')[3][3]=='-':
            line[0]=line[0].split('_')
            line[0][0]=line[0][0][:4]+'.ADE'
            line[0]='_'.join(line[0])
            #print(line[0])
            ade_file.write('\t'.join(line))
            continue
    elif cof2 in NAD:
        if line[1].split('_')[3][3]=='-':
            line[1]=line[1].split('_')
            line[1][0]=line[1][0][:4]+'.ADE'
            line[1]='_'.join(line[1][:3])
            #print(line[1])
            ade_file.write('\t'.join(line))
            continue
    line[0]='_'.join(line[0].split('_')[:3])
    line[1]='_'.join(line[1].split('_')[:3])
    out_file.write('\t'.join(line))


in_file=open('F:\span/align_all_ligands_and_nonredundant_metal_filterd.txt','r')
for line in in_file:
    for line in in_file:
        line=line.split('\t')
        cof1=line[0].split('_')[0]
        cof2=line[1].split('_')[0]
        cof1=cof1.split('.')[1]
        cof2=cof2.split('.')[1]
        line[2]=cof1
        line[3]=cof2
        line[6]=cof1+'_'+cof1
        line[0]='_'.join(line[0].split('_')[:3])
        line[1]='_'.join(line[1].split('_')[:3])
        out_file.write('\t'.join(line))
#

ade_file.close()
out_file.close()
#'''