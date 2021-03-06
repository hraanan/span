
import sys
import time
import Bio
from Bio import PDB
from Bio.PDB import PDBIO
from Bio.PDB import PDBParser
from Bio.PDB.PDBParser import PDBParser

from Bio import Entrez
from Bio.PDB import PDBList
from Bio.PDB import parse_pdb_header

pdbl = PDBList()
exitFlag = 0
taxonomy={}


def get_tax_data(taxid):
    """get taxonomy from taxid"""
    Entrez.email = "hraanan@gmail.com"    
    search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
    return Entrez.read(search)

in_file_name=sys.argv[1]
#in_file_name='F:\programs\span\data\pdbs_list_test.txt'


in_file=open(in_file_name,'r')
out_file=open(in_file_name+'_out.txt','w')
pdb_list=[]
old_pdb_list=[]
i=0


for line in in_file:
    i=i+1
    #if i>10:
     #   break
    protein=line[0:4]
    if protein not in pdb_list:# and protein not in old_pdb_list:
        pdb_list.append(protein)

print(len(pdb_list))       
        
for protein in pdb_list:
        print(protein)
        parser = PDB.PDBParser(PERMISSIVE=1,get_header=1,QUIET=1)
        rootdir ='/scratch/hr253/pdb_download_8_2018/pdb/'
        
        try:
            structure = parser.get_structure(protein,rootdir+protein[1:3]+'/pdb'+protein+'.ent')
        except:# FileNotFoundError:
            #try:
                out_file.write(protein+'\t'+'cofactor'+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')
                continue
                #pdbl.retrieve_pdb_file(protein,pdir=rootdir+protein[1:3])
                #structure = parser.get_structure(protein,rootdir+protein[1:3]+'/pdb'+protein+'.ent')
            #except:
                #out_file.write(protein+'\t'+'cofactor'+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')
        try:
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
            #print(EC)
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
                
            out_file.write(protein+'\t'+'cofactor'+'\t'+EC+'\t'+head+'\t'+molecule+'\t'+organism_scientific+'\t'+no_rank+'\t'+superkingdom+'\t'+phylum+'\t'+tclass+'\t'+order+'\t'+family+'\t'+genus+'\t'+organism_taxid+'\t'+name+'\t'+chains+'\t'+resolution+'\t'+structure_method+'\t'+keywords+'\t'+journal_reference+'\t'+release_date+'\n')
        except:
            out_file.write(protein+'\t'+'cofactor'+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')
print('end')
out_file.close()
in_file.close()

