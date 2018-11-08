

''' 

This program gets exactly 2 arg!

1. extract list of cofactors from file 
2. open PDBs and get the coordinats of each cofactor that in the list.
3. if there are more than 1 cofactor in the PDB make list of the cofactor pairs that in distance of less than min_dis 

important variables:
proteins_list= list of PDBs
lig= list of cofactor deatils (strings) 
ligands = list of lig's 
dis_min=20 # the minimal distance between cofactor to include in chain
nebrs= list of pers of cofactor in distance less than min_dis (i,j)
nebrsdis=list of pers of cofactor in distance less than min_dis include the distance (i,j,dis)
'''



import math
import os
from Bio import PDB
pdbl=PDB.PDBList()


def get_center(atom_coord_list):
    x=0
    y=0
    z=0    
    for atom in atom_coord_list:
        
        x=x+atom[0]
        y=y+atom[1]
        z=z+atom[2]
    #print(x,y,z)    
    try:
            x=x/len(atom_coord_list)
            y=y/len(atom_coord_list)
            z=z/len(atom_coord_list)
            center=numpy.array([x,y,z])
    except:
               
            x=10000
            y=10000
            z=10000
    center=numpy.array([x,y,z])
    return center;
    
NAD=['NAD','ADJ','ENP','NAP','NDP','NJP','NZQ','XNP']
al_file=open('center_atom_list.txt','r')
al_file.readline()
al_dict={}
for line in al_file:
    line=line.split('\t') 
    al_dict[line[0]]=line[1][:-1]
#
#if len(sys.argv)!=3:
#    print('This program gets exactly 2 arg!')
#    exit()
## Variables
#print (sys.argv[1],sys.argv[2])
from_line=0#int(sys.argv[1])
to_line=100700#int(sys.argv[2])
protein_list=[]
ec_list=[]
metal_cofactors={}
cofactors_group={}
cofactors_file=open('wt_taxonomy_groups_align_organicNewCenter_all_nonredundant_with_factor_ca_10_md_3_rmsd_5_with_factor_1.3.txt','r')
cofactors_file.readline()
for line in cofactors_file:
    line=line.split('\t')    
    key=line[0].split('_')
       
    if line[2] in NAD and key[3][0:3]==line[2]:
        line[2]='ADE'
        
    key='_'.join(key[:3])
    key=key.replace('.','_')      
    cofactors_group[key]=line[1]    
    metal_cofactors[key]=line[2]    
    ec=line[3]    
    ec_split=ec.split('.')
    try:    
        ec1=ec_split[0]
        ec2=ec_split[1]
        ec3=ec_split[2]
        ec4=ec_split[3]
    except:
        ec1=0
        ec2=0
        ec3=0
        ec4=0
    protein=key[0:4]    
    
        
    if protein not in protein_list:
        protein_list.append(protein)
        ec_list.append(ec)
cofactors_file=open('wt_taxonomy_groups_align_onoredundant_chl_and_heme_new_center_ca_10_md_3_rmsd_5_with_factor_1.15.txt','r')
cofactors_file.readline()
for line in cofactors_file:
    line=line.split('\t')    
    key=line[0].split('_')
    ec=line[3]    
    ec_split=ec.split('.')
    try:    
        ec1=ec_split[0]
        ec2=ec_split[1]
        ec3=ec_split[2]
        ec4=ec_split[3]
    except:
        ec1=0
        ec2=0
        ec3=0
        ec4=0
    protein=key[0]    
    key='_'.join(key[:3])
    key=key.replace('.','_')    
    #print (key)    
    metal_cofactors[key]=line[2]
    cofactors_group[key]=line[1]
    protein=protein.split('.')
    protein=protein[0]
    if protein not in protein_list:
        protein_list.append(protein)
        ec_list.append(ec)
cofactors_file=open('clean_group_file_ca_10_md_3_rmsd_5_factor_1.4.txt','r')
cofactors_file.readline()
for line in cofactors_file:
    line=line.split('\t')    
    key=line[0].split('_')
    ec=line[3]    
    ec_split=ec.split('.')
    try:    
        ec1=ec_split[0]
        ec2=ec_split[1]
        ec3=ec_split[2]
        ec4=ec_split[3]
    except:
        ec1=0
        ec2=0
        ec3=0
        ec4=0
    protein=key[0]    
    key='_'.join(key[:3])
    key=key.replace('.','_')    
    #print (key)    
    metal_cofactors[key]=line[2]
    cofactors_group[key]=line[1]
    protein=protein.split('.')
    protein=protein[0]
    if protein not in protein_list:
        protein_list.append(protein)
        ec_list.append(ec)


dis_max=14 # the minimal distance between cofactor to include in chain
dis_min=4.5
AA=['PHE','TRP','TYR','ALA','CYS','ASP','GLU','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL']
CF=[' DA',' DC',' DG',' DT','  A','  C','  G','  U','HOH','UNK','DOD'] # list of cofactor to ignore
#Metals=['ZN','FE','CA','NA','MN','K','CU','OS','SR','CO','NI','W','PT','MO','BA','CS','BE','U','TA','V','TL','AL','AU','IR','Y','GD','RB','RU','PB','YB','SM','LI','PD','AG','EU','RH','PR','RE','LU','TB','HF','HO','DY','ZR','CR','LA','GA','SB','SN','CE','ER','AM','CM','IN','TH','PU','SC','BI','PA']
Metals=['ZN','FE','CA','NA','MN','K','CU','OS','SR','CO','NI','W','PT','MO','BA','CS','BE','U','TA','V','TL','AL','AU','IR','Y','GD','RB','RU','PB','YB','SM','LI','PD','AG','EU','RH','PR','RE','LU','TB','HF','HO','DY','ZR','CR','LA','GA','SB','SN','CE','ER','AM','CM','IN','TH','PU','SC','BI','PA']
chl=['BCB','BCL','CHL','CL0','CLA','PHO','PMR','BPB','BPH']
heme=['B12','CNC','COH','DHE','F43','HAS','HDD','HDE','HEA','HEC','HEM','SRM']
pyr_atom_list=['C3A','C3B','C3C','C3D']

Distance=[]

Allchains=open('organic_cofactor_distance_counts_4.5+.txt','w')#"chain_from_"+sys.argv[1]+'_to_'+sys.argv[2]+'.txt',"w") # Output file
Allchains.write('source\ttarget\tweight\n')
Alledges_file=open('organic_cofactor_distance_edges_4.5+.txt','w')#"chain_from_"+sys.argv[1]+'_to_'+sys.argv[2]+'.txt',"w") # Output file
#Alledges_file.write('source\ttarget\tdistance\tprotein\n')
#ec_file=open('nonredundant_distance_counts_ec4_4.5+.txt','w')#"chain_from_"+sys.argv[1]+'_to_'+sys.argv[2]+'.txt',"w") # Output file
Alledges_file.write('source\ttarget\tdistance\tprotein\tec\n')

# make protein list
#idxfile='/home/hraanan/pdb_download/entries.idx.txt'
#idx=open(idxfile,"r")
#idx.readline()
#idx.readline()
#idx.readline()
edges={}
ecs={}
#Allchains.write('Group 1\tGroup 2\tNumber of edges\n') '4xk8',

#protein_list=['4ac5','1h0h','2fdn','3qiy']
for prot_index,protein in enumerate(protein_list):
    ec=ec_list[protein_list.index(protein)]
    if prot_index < from_line:
        continue
    if prot_index >= to_line:
        break
    print('prot_index:'+str(prot_index))
#    protein=line[0:4]
#    protein=protein.lower()
    #print ('pdb_code',protein)
    #protein='1h0h'
    parser = PDB.PDBParser(PERMISSIVE=1)
    structure = parser.get_structure(protein,'/home/hraanan/pdb_download/'+protein[1:3]+'/pdb'+protein+'.ent')
    cofactor_dic={}
    proteins_list=[]

    #parser = PDB.PDBParser(PERMISSIVE=1)
    curdir=os.getcwd()
#    print (protein,curdir+'/'+protein[1:3]+'/pdb'+protein+'.ent')
    #structure = parser.get_structure(protein,'/home/hraanan/pdb_download/'+protein[1:3]+'/pdb'+protein+'.ent')
    head= structure.header['head']
    comp = structure.header['compound']
    
    sf4ID=[]
    sf4coord=[]
# make list of cofactors 
    for model in structure:
        if model.id==0:
         Ligands=[]
         lig=[]
         sf4ID=[]
         sf4coord=[]
         clusters=[]
         for chain in model:
              
              for residue in chain:
                 
                 res_id=protein+'_'+residue.resname+'_'+chain.id+'_'+str(residue.id[1])
                 res_id=res_id.replace(" ","")                    
#                 if residue.resname not in AA and residue.resname not in CF:
#                   #  print ('res_id:'+res_id)                    
                 if res_id in cofactors_group.keys():
                    #print(chain.id,residue.id)
                    coord = []
                    
# get cofactor center                                        
                    if residue.resname not in chl and residue.resname not in heme:                    
                        for atom in residue:
                        #   print(atom.coord)
                            
                           at=atom.coord
                           x=at[0]
                           y=at[1]
                           z=at[2]
                           atcord=[x,y,z]
                           coord.append(atcord)
                        x=0
                        y=0
                        z=0
                        i=0
                        for point in coord:
                            i=i+1
                            x=x+point[0]
                            y=y+point[1]
                            z=z+point[2]
                        x=x/i
                        y=y/i
                        z=z/i
                       # c=numpy.array([x,y,z])+str(x)+','+str(y)+','+str(z)
                        lig=protein,chain.id,residue.id[1],cofactors_group.get(res_id),x,y,z,coord,metal_cofactors.get(res_id)  # lig= list of cofactor deatils (strings) 
                       # print(lig)
                        Ligands.append(lig)
                        #Dist.write(protein+','+chain.id+','+str(residue.id[1])+','+residue.resname+','+str(x)+','+str(y)+','+str(z)+'\n')
    #         for i in Ligands:
    #            print(i)                  
                    if residue.resname in chl or residue.resname in heme:                    
                                                                    
                        for atom in residue:
                           if atom.name in pyr_atom_list or atom.name[0]=='O' or atom.name=='MG' or atom.name=='FE':
                            #   print(atom.coord)
                                
                            #   print(atom.name)
                               at=atom.coord
                               x=at[0]
                               y=at[1]
                               z=at[2]
                               atcord=[x,y,z]
                               coord.append(atcord)
                        x=0
                        y=0
                        z=0
                        i=0
                        for point in coord:
                            i=i+1
                            x=x+point[0]
                            y=y+point[1]
                            z=z+point[2]
                        x=x/i
                        y=y/i
                        z=z/i
                       # c=numpy.array([x,y,z])+str(x)+','+str(y)+','+str(z)
                        lig=protein,chain.id,residue.id[1],cofactors_group.get(res_id),x,y,z,coord,metal_cofactors.get(res_id)  # lig= list of cofactor deatils (strings) 
                       # print(lig)
                        Ligands.append(lig)
                        #Dist.write(protein+','+chain.id+','+str(residue.id[1])+','+residue.resname+','+str(x)+','+str(y)+','+str(z)+'\n')
                    if residue.resname in al_dict.items():
                        al=al_dict[residue.resname][0]
                        for atom in residue:
                           if atom.name in al or al=='all':
                            #   print(atom.coord)
                                
                            #   print(atom.name)
                               at=atom.coord
                               x=at[0]
                               y=at[1]
                               z=at[2]
                               atcord=[x,y,z]
                               coord.append(atcord)
                        x=0
                        y=0
                        z=0
                        i=0
                        for point in coord:
                            i=i+1
                            x=x+point[0]
                            y=y+point[1]
                            z=z+point[2]
                        x=x/i
                        y=y/i
                        z=z/i
                       # c=numpy.array([x,y,z])+str(x)+','+str(y)+','+str(z)
                        lig=protein,chain.id,residue.id[1],cofactors_group.get(res_id),x,y,z,coord,metal_cofactors.get(res_id)  # lig= list of cofactor deatils (strings) 
                       # print(lig)
                        Ligands.append(lig)                        
                        if len(al_dict[residue.resname])>1:
                            al=al_dict[residue.resname][1]
                            for atom in residue:
                               if atom.name in al:
                                #   print(atom.coord)
                                    
                                #   print(atom.name)
                                   at=atom.coord
                                   x=at[0]
                                   y=at[1]
                                   z=at[2]
                                   atcord=[x,y,z]
                                   coord.append(atcord)
                            x=0
                            y=0
                            z=0
                            i=0
                            for point in coord:
                                i=i+1
                                x=x+point[0]
                                y=y+point[1]
                                z=z+point[2]
                            x=x/i
                            y=y/i
                            z=z/i
                           # c=numpy.array([x,y,z])+str(x)+','+str(y)+','+str(z)
                            res_id=protein+'_'+'ADE'+'_'+chain.id+'_'+str(residue.id[1])
                            res_id=res_id.replace(" ","")                              
                            lig=protein,chain.id,residue.id[1],cofactors_group.get(res_id),x,y,z,coord,metal_cofactors.get(res_id)  # lig= list of cofactor deatils (strings) 
                           # print(lig)
                            Ligands.append(lig)                
                            
                        
    #         for i in Ligands:
    #            print(i)                  

    x=[]
    y=[]
    z=[]
    nebrs=[]
    nebrsdis=[]
    allperdis=[]
    allper=[]  
#make list of x's y's z's of all cofactors in the PDB
    for cluster in Ligands:
        x.append(cluster[4])
        y.append(cluster[5])
        z.append(cluster[6])
        
# if there are more than 1 cofactor in the PDB make list of the cofactor pers that in distance of less than min_dis 
    if len(x)>1 :
        
        for i in range(0,len(x)):
         
           atoms_i=Ligands[i][7]    
  #         print(i)    
           for j in range(0,len(x)):
               
                  #  print(i,j)
                   # Dis=math.sqrt((pow((x[i]-x[j]),2))+(pow((y[i]-y[j]),2))+(pow((z[i]-z[j]),2)))
                                        
                    if i==j:
                        continue
                    atoms_j=Ligands[j][7]    
                    Dis=100
                    for at_i in atoms_i:
                        for at_j in atoms_j:
                            if at_i==at_j:
                                continue
                            #print (at_i[0],at_j[0])
                            at_dis=math.sqrt((pow((at_i[0]-at_j[0]),2))+(pow((at_i[1]-at_j[1]),2))+(pow((at_i[2]-at_j[2]),2)))    
                            if at_dis<Dis:
                                Dis=at_dis
                                                               
                                #print('Dis:')
                                #print(at_dis)
                    n=[i,j]
                    allper.append(n)
                    n=[i,j,Dis]
                    allperdis.append(n)
                                        
                    if Dis>dis_min and Dis<dis_max:
#                        print(i,j)                         
#                        print('Dis:')
#                        print(Dis)
                        n=[i,j]
                        nebrs.append(n)
                        n=[i,j,Dis]
                        nebrsdis.append(n)
                        

    for x in range (0,len(Ligands)):
        Ligands[x]=Ligands[x]+(x,)
      #  print(Ligands[x])
    onesidenebrs=[]
    cng=0
    for j in range(len(Ligands)):
                i=Ligands[j]
               # print('--',i[0],i[7],i[3],i[1],i[2])
                

    for i in nebrs:
        if i not in onesidenebrs and i[::-1] not in onesidenebrs and int(i[0])!=int(i[1]):
            onesidenebrs.append(i)
    onesidenebrsdis=[]
    for i in onesidenebrs:
        for j in nebrsdis:
            if i[0]==j[0] and i[1]==j[1]:
                onesidenebrsdis.append(j)
    
    for i in nebrs:
        #print(i)
        if int(i[0])==int(i[1]):
            nebrs.remove(i)
    print('Done neighbors procsses...............')
   # print('nebrs:',nebrs)
    

    chain=[]
    groups=[]
    lignebrs=[]
##    for i in Ligands:
##      print(i)
    for i in range(0,len(Ligands)):
        lignebrs.append([]) 
        for j in onesidenebrs:
            if j[0]==i and j[1] not in lignebrs[i]:
                lignebrs[i].append(j[1])
            if j[1]==i and j[0] not in lignebrs[i]:
                lignebrs[i].append(j[0])
 #   print ('onesidenebrs:',onesidenebrsdis)
    for i in onesidenebrsdis:
        fst=Ligands[i[0]][3]+';'+Ligands[i[0]][8]
        scd=Ligands[i[1]][3]+';'+Ligands[i[1]][8]
#        x=[Ligands[i[0]][4],Ligands[i[1]][4]]
#        y=[Ligands[i[0]][5],Ligands[i[1]][5]]
#        z=[Ligands[i[0]][6],Ligands[i[1]][6]]        
#        Dis=math.sqrt((pow((x[0]-x[1]),2))+(pow((y[0]-y[1]),2))+(pow((z[0]-z[1]),2)))        
        dis=i[2]        
        key=[fst,scd]
        if Ligands[i[0]][3] != Ligands[i[1]][3]:
            key=sorted(key)
        key[0]=key[0].split(';')
        key[1]=key[1].split(';')
        Alledges_file.write(key[0][0]+'\t'+key[1][0]+'\t'+key[0][1]+'\t'+key[1][1]+'\t'+str(dis)+'\t'+protein+'\t'+ec+'\n')          
        edge=key[0][0]+'-'+key[1][0]
        key=edge
        if key in edges:
            edges[key] += 1
        else:
            edges[key] = 1
        if key in ecs:
            if ec not in ecs.get(key):
                x= ecs.get(key)  
                x.append(ec)
                ecs[key]=x
        if key not in ecs:
            ecs[key]=[ec]
       
        

for key,value in edges.items():
    key=key.split('-')    
    Allchains.write(key[0]+'\t'+key[1]+'\t'+str(value)+'\n')
for key,value in ecs.items():
    key=key.split('-')    
#    counts_ecs=[]    
#    for i in value:
#        if i not in counts_ecs:
            
#    ec_file.write(key[0]+'\t'+key[1]+'\t'+str(len(value))+'\t'+str(';'.join(value))+'\n')
    
Allchains.close()
Alledges_file.close()

#ec_file.close()

cofactors_file.close()
print("end")

