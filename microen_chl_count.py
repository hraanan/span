# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:35:48 2017

@author: hraanan
"""
from Bio import PDB
parser = PDB.PDBParser()


d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
     
chl=['BCB','BCL','CHL','CL0','CLA','PHO','PMR','BPB','BPH']
#out_file=open('seq.txt','w')
in_file=open('microenvironments_metadata.txt','r')
out_file=open('chl_aa_ratio.txt','w')
chl_list=[]
for line in in_file:
    line=line.split('\t')
    if line[3]=="Chl":
        chl_list.append(line[0])
        
for microen in chl_list:
  # try:
    
    dirname=microen.split('_')[0]
    dirname=dirname.split('.')[1]    
    structure = parser.get_structure('pdb','F:\microfolds_8_2018/new_all/'+dirname+'/'+microen+'.pdb') 
    model = structure[0]
    res_no = 0
    non_resi = 0
    #in_file=open('/home/hraanan/MicrofoldsPDBs/ChlorophyllNewCenter/'+dirname+'/'+filename,'r')
    for model in structure:
       
            
        for residue in model.get_residues():
            if PDB.is_aa(residue):
                res_no += 1
    
            elif residue.resname in chl:
                non_resi += 1
        
       # print ("Residues2: %i" % (res_no))
       # print ("Other2:    %i" % (non_resi)) 
        ratio=res_no/non_resi 
        out_file.write(microen+'\t'+str(res_no)+'\t'+str(non_resi)+'\t'+str(ratio)+'\n')
out_file.close()
print('end')
