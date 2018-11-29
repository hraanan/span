# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:35:48 2017

@author: hraanan
"""
from Bio import PDB
parser = PDB.PDBParser()
import center
import os

def foo(path):
    path=path+'/'
    return os.listdir(path)[0]
d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
Metals=['FE','MN','CU','CO','NI','W','MO','V']     
in_file=open('F:\span_26.11.18/cofactor_list.txt','r')
out_file=open('cofactor_metal_content.txt','w')
rootdir='F:\microfolds_8_2018/new_all/'
        
for line in in_file:
  # try:
      line=line[:-1]
      dirname=line
      
      if center.is_in_list(dirname)==False:
          file_name=foo(rootdir+line)
          structure = parser.get_structure('pdb',rootdir+line+'/'+file_name) 
          model = structure[0]
          print(dirname)
          for chain in model:
              metals_in_cof=[]
              for residue in chain:
                  if residue.resname.strip()==dirname:
                      for atom in residue:
                          
                          if atom.element in Metals or atom.element=='S':
                              if atom.element not in metals_in_cof:
                                  metals_in_cof.append(atom.element)
                      print(metals_in_cof)
                      s=False
                      fe=False
                      for at in metals_in_cof:
                          if at=='FE':
                              fe=True
                          if at=='S':
                              s=True
                      if fe==True and s==True:
                            metals_in_cof=['FES']
#                          
                      out_file.write(line+'\t'+';'.join(metals_in_cof)+'\n')
                      break
                  

out_file.close()
print('end')
