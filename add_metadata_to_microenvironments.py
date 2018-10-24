# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:36:09 2018

@author: hraanan
"""


import Bio

from Bio import PDB
from Bio.PDB import PDBIO
from Bio.PDB.PDBParser import PDBParser

from Bio.PDB import *
import sys
from Bio import Entrez

def get_tax_data(taxid):
    """get taxonomy from taxid"""
    Entrez.email = "hraanan@gmail.com"    
    search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
    return Entrez.read(search)

group_file=open('f:/span/full_list_of_microenvironments_align_all_no_ADE_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','r')
out_file=open('f:/span/full_list_of_microenvironments_data_align_all_no_ADE_2016_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4.txt','w')



#Entrez.email = "hraanan@gmail.com"    
taxonomy={}

group_file.readline()
out_file.write('id\tcofactor\tec\thead\tmolecule\torganism_scientific\tno rank\tsuperkingdom\tphylum\tclass\torder\tfamily\tgenus\torganism_taxid\tname\tchains\tresolution\tstructure_method\tkeywords\tjournal_reference\trelease_date\n')

#out_file.write('id\tcofactor\tec\thead\tmolecule\torganism_scientific\tname\tchains\tresolution\tstructure_method\tkeywords\tjournal_reference\trelease_date\n')
#out_file.write(line[:-1]+'\t'+cofactor+'\t'+EC+'\t'+head+'\t'+molecule+'\t'+organism_scientific+'\t'+name+'\t'+chains+'\t'+resolution+'\t'+structure_method+'\t'+keywords+'\t'+journal_reference+'\t'+release_date+'\n')
        #print(i)
i=0
z=0
for line in group_file:
  #  try:
        i=i+1
        protein=line[0:4]
        #line=line.split('\t')
        parser = PDB.PDBParser(PERMISSIVE=1,get_header=1,QUIET=1)
        cofactor=line[:-1].split('_')
        
        cofactor=cofactor[0].split('.')
        cofactor=cofactor[1]
        rootdir ='f:/pdb_download_8_2018/pdb/'
        structure = parser.get_structure(protein,rootdir+protein[1:3]+'/pdb'+protein+'.ent')
        head= structure.header['head']
        comp = structure.header['compound']
        # Reading EC number from the pdb header
        EC=""
        try:
            comp=comp['1']
        except KeyError:
            EC='-.-.-.-'
        try:
            EC=comp['ec']
        except KeyError:
             pass
        try:
            EC=comp['ec_number']
        except KeyError:
            pass
        if EC=="": 
            EC='-.-.-.-'
        handle = open(rootdir+protein[1:3]+'/pdb'+protein+'.ent','r')
        header_dict = parse_pdb_header(handle)
        handle.close()
        print(EC)
        vars=['author','compound','chains','molecule','head','resolution','release_date','keywords','journal_reference','name','source','organism_scientific','organism_taxid','structure_method']  
        
        author=header_dict.get('author',"empty")
            
        compound=header_dict.get('compound',"empty")
        if compound is None:
            chains="empty"
            molecule="empty"
        else:
            compound=compound.get('1',"empty")
            if compound is None:
                chains="empty"
                molecule="empty"
            chains=compound.get('chain',"empty")
            if chains is None: 
                chains="empty"
            molecule=compound.get('molecule')
            if molecule is None: 
                molecule="empty"
        source=header_dict.get('source')    
        if source is None:
            organism_scientific="empty"
            organism_taxid="empty"    
        else:
            source=source.get('1')
            if source is None:
                organism_scientific="empty"
                organism_taxid="empty"   
            organism_scientific=source.get('organism_scientific')
            if organism_scientific is None: 
                 organism_scientific="empty"
            organism_taxid=source.get('organism_taxid',"empty")
            if organism_taxid is None: 
                 organism_taxid="empty"    
        head=header_dict.get('head',"empty")
        if head is None: 
                head="empty"    
        resolution=str(header_dict.get('resolution','empty'))
        if resolution is None: 
                resolution="empty" 
        release_date=header_dict.get('release_date',"empty")
        if release_date is None: 
                release_date="empty"     
        keywords=header_dict.get('keywords',"empty")
        if keywords is None: 
                keywords="empty"         
        journal_reference=header_dict.get('journal_reference',"empty")
        if journal_reference is None: 
                journal_reference="empty"          
        name=header_dict.get('name',"empty")
        if name is None: 
                name="empty"            
        structure_method=header_dict.get('structure_method',"empty")
        if structure_method is None: 
                structure_method="empty"       
        
        for var in vars:
            var.replace('\t',';')
        
        if organism_taxid != 'empty':
            if organism_taxid not in taxonomy:
                try:        
                    #Entrez.email = "hraanan@marine.rutgers.edu"
                    data = get_tax_data(organism_taxid)
                    lineage = {d['Rank']:d['ScientificName'] for d in data[0]['LineageEx'] if d['Rank'] in ['no rank','superkingdom','phylum','class', 'order','family','genus']} 
                    taxonomy[organism_taxid]=lineage
                except:
                    lineage ={}
            lineage=taxonomy.get(organism_taxid)
            no_rank=lineage.get('no rank','empty')
            superkingdom=lineage.get('superkingdom','empty')
            phylum=lineage.get('phylum','empty')
            tclass=lineage.get('class','empty')
            order=lineage.get('order','empty')
            family=lineage.get('family','empty')
            genus=lineage.get('genus','empty')
        else:
            no_rank='empty'
            superkingdom='empty'
            phylum='empty'
            tclass='empty'
            order='empty'
            family='empty'
            genus='empty'
            
        #print('\t'.join(line[0:4])+'\t'+cofactor+'\t'+line[5]+'\t'+head+'\t'+molecule+'\t'+organism_scientific+'\t'+no_rank+'\t'+superkingdom+'\t'+phylum+'\t'+tclass+'\t'+order+'\t'+family+'\t'+genus+'\t'+organism_taxid+'\t'+name+'\t'+chains+'\t'+resolution+'\t'+structure_method+'\t'+keywords+'\t'+journal_reference+'\t'+release_date+'\n')    
            
        out_file.write(line[:-1]+'\t'+cofactor+'\t'+EC+'\t'+head+'\t'+molecule+'\t'+organism_scientific+'\t'+no_rank+'\t'+superkingdom+'\t'+phylum+'\t'+tclass+'\t'+order+'\t'+family+'\t'+genus+'\t'+organism_taxid+'\t'+name+'\t'+chains+'\t'+resolution+'\t'+structure_method+'\t'+keywords+'\t'+journal_reference+'\t'+release_date+'\n')
   
       # out_file.write(line[:-1]+'\t'+cofactor+'\t'+EC+'\t'+head+'\t'+molecule+'\t'+organism_scientific+'\t'+name+'\t'+chains+'\t'+resolution+'\t'+structure_method+'\t'+keywords+'\t'+journal_reference+'\t'+release_date+'\n')
        #print(i)
 #   except:
  #      z=z+1
        #print(line)
   #     continue

out_file.close()
print('errs',i)
print('of',i)
print('end')