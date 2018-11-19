import Bio
import os
import sys
from Bio import PDB
from Bio.PDB import PDBIO
from Bio.PDB.PDBParser import PDBParser
import math
import numpy
from collections import Counter
import random 
from Bio.PDB import *
import gzip
import center

    

######initial variabels############# 
#rootdir='/scratch/hr253/pdb_download_8_2018/pdb/' # folder of the dpb files
microfold_root='f:/microfolds_8_2018/new_all/'
if not os.path.exists(microfold_root):
    os.makedirs(microfold_root)
rootdir ='f:/pdb_download_8_2018/pdb/' # folder of the pdb original filesdownladed form the pdb
i=0
EC=""
cng=0     
fd=['1fdn'] # used to test script on knowen pdb file
AA=['PHE','TRP','TYR','ALA','CYS','ASP','GLU','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL']
CF=[' DA',' DC',' DG',' DT','  A','  C','  G','  U','HOH','UNK','UNX'] # list of cofactor names to ignore
Metals=['FE','MN','CU','CO','NI','W','MO','V'] 
chl=['BCB','CLA','CHL','BCL','CL0','PMR','PHO'] #chlorophyll cofactors list
heme=['HEA','HAS','2FH','522','89R','DDH','DHE','HES','HDD','HDE','HDM','HEB','HEC','HEM','HEO','HEV','HP5','MH0','N7H','NTE','OBV','SRM','VER']
pyr_atom_list=['C3A','C3B','C3C','C3D']
NAD=['NAD','ADJ','ENP','NAP','NDP','NJP','NZQ','XNP']

#####################
def save_microfold(microfold_name,all_neighbors):
    if not os.path.exists(microfold_root+microfold_dir):
        os.makedirs(microfold_root+microfold_dir)
    Select = Bio.PDB.Select
    class MicroSelect(Select):
        def accept_residue(self, residue):
            if residue in all_neighbors and residue.resname!='HOH':
                return 1
            else:
                return 0
    i=0
    for residue in all_neighbors:
        if residue.resname in AA:
            i=i+1
    if i>10:        
        io=PDBIO()
        io.set_structure(structure)
        io.save(microfold_root+microfold_dir+'/'+microfold_name+'.pdb', MicroSelect())
    

pdbl=PDB.PDBList()
#Error_out=open("microfolds_out.txt","w")


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            # loding pdb file
            line=file
            protein=line[3:7]
            #print ('pdb_code:'+protein)
            protein=protein.lower()
           # Error_out.write('pdb_code:'+protein+'\n')
        
            parser = PDB.PDBParser(PERMISSIVE=1,get_header=1,QUIET=1)
            #curdir=os.getcwd()
            #filename=rootdir+protein[1:3]+'/'+file
            #print(filename)
            
            final_file=rootdir+protein[1:3]+'/pdb'+protein+'.ent'
            
            # unzipping gz file 
            #gz = gzip.open(filename, 'rb') 
            #with open(final_file, 'wb') as out: 
            #    out.writelines(gz) 
            #gz.close()
            #print ('unziping done')
            
            
            # openning pdb file 
            structure = parser.get_structure(protein,rootdir+protein[1:3]+'/pdb'+protein+'.ent')
            
            for model in structure:
                if model.id==0:
                 atom_list = Selection.unfold_entities(model, 'A') # A for atoms
                 ns = NeighborSearch(atom_list)
                 lig=[]
                 for chain in model:
                     for residue in chain:
                
                          if residue.resname not in AA and residue.resname not in CF:
                              #print(chain.id,residue.resname)
                              
                              if center.is_in_list(residue.resname)==True:
                                  atom_list=center.get_atom_list(residue.resname)
                                  atom_coord_list=center.get_atom_coord_list(residue,atom_list)
                                  cof_center = center.get_center(atom_coord_list)
                                  #print ('center',center)
                                  lig=protein,chain.id,residue.id[1],residue.resname,cof_center
                                  #print(lig)
                                  all_neighbors = ns.search(cof_center, 15.0,"R") # 15.0 for distance in angstrom
                                  microfold_name=protein+'.'+residue.resname+'_'+ chain.id +'_'+str(residue.id[1])
                                  microfold_name=microfold_name.replace(' ','')
                                  microfold_name=microfold_name.replace('/','_')
                                  microfold_dir=residue.resname
                                  microfold_dir=microfold_dir.replace(' ','')                                                            
                                  
                                  save_microfold(microfold_name,all_neighbors)
                                  
                                  if center.has_ade(residue.resname)==True:
                                      atom_list=center.get_atom_list('ADE_'+residue.resname)
                                      atom_coord_list=center.get_atom_coord_list(residue,atom_list)
                                      cof_center = center.get_center(atom_coord_list)
                                      #print ('center',center)
                                      lig=protein,chain.id,residue.id[1],residue.resname,cof_center
                                      #print(lig)
                                      all_neighbors = ns.search(cof_center, 15.0,"R") # 15.0 for distance in angstrom
                                      microfold_name=protein+'.ADE_'+residue.resname+'_'+ chain.id +'_'+str(residue.id[1])
                                      microfold_name=microfold_name.replace(' ','')
                                      microfold_name=microfold_name.replace('/','_')
                                      microfold_dir='ADE'
                                      microfold_dir=microfold_dir.replace(' ','')
                                      save_microfold(microfold_name,all_neighbors)
                                      atom_in_res=[]
                              else:
                                  atom_in_res=[]
                                  for atom in residue:
                                      atom_in_res.append(atom.element)
                                  if any(x in Metals for x in atom_in_res)==False:
                                      #print ('not metal')
                                       continue
                                  atom_list=['all']
                                  atom_coord_list=center.get_atom_coord_list(residue,atom_list)
                                  cof_center = center.get_center(atom_coord_list)
                                  #print ('center',center)
                                  lig=protein,chain.id,residue.id[1],residue.resname,cof_center
                                  #print(lig)
                                  all_neighbors = ns.search(cof_center, 15.0,"R") # 15.0 for distance in angstrom
                                  microfold_name=protein+'.'+residue.resname+'_'+ chain.id +'_'+str(residue.id[1])
                                  microfold_name=microfold_name.replace(' ','')
                                  microfold_name=microfold_name.replace('/','_')
                                  microfold_dir=residue.resname
                                  microfold_dir=microfold_dir.replace(' ','')                                                            
                                  
                                  save_microfold(microfold_name,all_neighbors)
                                
        except:
            
#            Error_out.write( protein )
            print(protein)
            continue
#                               
    
#Error_out.close()
#prot.close()
print("end")
