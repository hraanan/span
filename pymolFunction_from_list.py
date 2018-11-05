#!/usr/bin/python
import os

from pymol import stored
from pymol import cmd
from time import sleep
import numpy 
import sys
import time

        
import resource

def file_len(count_file_name):
    lines=0
    count_file=open(count_file_name,'r')
    for line in count_file:
        lines=lines+1
    
    count_file.close()
    return lines

def get_center(atom_coord_list):
    x=0
    y=0
    z=0    
        
    for atom in atom_coord_list:
        
        x=x+atom[0]
        y=y+atom[1]
        z=z+atom[2]
        
    try:
            x=x/len(atom_coord_list)
            y=y/len(atom_coord_list)
            z=z/len(atom_coord_list)
            center=numpy.array([x,y,z])
    except:
            return 'NA'   
    center=numpy.array([x,y,z])
    return center;

#in_file_name=sys.argv[1]
#in_file_name='/home/hraanan/span/align_lists/align_cofactors.txt'
#in_file=open(in_file_name,'r')
#print(in_file_name)
microen_dir='/home/hraanan/microfolds_8_2018/all/'

#out_file_name=in_file_name[:-4]+'_out.txt' #_'+in_file_name.split('.')[1]+'.txt'
#out_file=open(out_file_name,'w')              
#out_file.write('Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance'+'\t'+'Structural Distance'+'\n')
atoms_file=open('/home/hraanan/span/manual_cofactor_list_with_quinone_2_atoms_ADE.txt','r')
atoms_file.readline()
al_dict={}
for line in atoms_file:
    line=line.split('\t')
    if line[3]=='all':
        continue
    al_dict[line[1]]=[line[3],line[4][:-1]]



def pyFunc(in_file_name):
    #cmd.set max_threads, 1    
    in_file=open(in_file_name,'r')
    print(in_file_name)
    
    count_file_name=in_file_name+'_count.txt'
    count_file_len=0
    if os.path.exists(count_file_name)==False:
        count_file=open(count_file_name,'w')
    else:
              
        count_file_len=file_len(count_file_name)
       
        count_file=open(count_file_name,'w')
    err_file_name=in_file_name+'_'+str(count_file_len)+'_err.txt'
    out_file_name=in_file_name+'_'+str(count_file_len)+'_out.txt' #_'+in_file_name.split('.')[1]+'.txt'
    out_file=open(out_file_name,'w')
    err_file=open(err_file_name,'w')
    
    
    #out_file.write('Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance'+'\t'+'Structural Distance'+'\n')
    
    t=0    
    for i in xrange(count_file_len):
        in_file.next()
    start = time.time()    
    print('start align from line: '+str(count_file_len))        
    for line in in_file:
       #print(line)        
       try:
            #s=time.time()                 
            count_file.write(str(t+count_file_len)+'\n')
            t=t+1
            #if t>200:
             #   break
            cmd.reinitialize()
            line=line.split('\t')
            microen1=line[0][:-4]
            microen2=line[1][:-6]
            
            #PDB2='3cw9.01A_B_991'
            lig1=line[0].split('_')[0]
            lig1=lig1.split('.')[1]
            PDB1=lig1.split('.')[0]
            
            lig2=line[1].split('_')[0]
            lig2=lig2.split('.')[1]
            PDB2=lig2.split('.')[0]
            
            Fldr1=microen_dir+lig1+'/'
            Fldr2=microen_dir+lig2+'/'
            pdbFile_1=str(Fldr1)+microen1+".pdb"
            pdbFile_2=str(Fldr2)+microen2+".pdb"
            cmd.load(pdbFile_1,'PDB1')	
            cmd.load(pdbFile_2,'PDB2')
            #print('load')
            Ql=cmd.count_atoms('PDB1 and name CA')
            Tl=cmd.count_atoms('PDB2 and name CA')
            #print('count')
            if Ql<10 or Tl<10:
                continue
            #print('Ql,Tl:'+str(Ql)+str(Tl))
            res_num1=microen1.split('_')
            res_num2=microen2.split('_')
           
            res_num1=res_num1[2]
            res_num2=res_num2[2]             
            #print('res_num1:',res_num1)                    
            #print('res_num2:',res_num2)
           
            x=cmd.align('PDB1 and name CA','PDB2 and name CA',quiet=1, cycles=5)
            #print('align')
            align_out=[x[0],x[1],x[5],x[6]]
            #print(align_out)
            atomlist=[]                    
            #print(PDB1,PDB2) 
            if lig1 not in al_dict:
                center1=get_center(cmd.get_model('PDB1 and resi '+res_num1, 1).get_coord_list())
            else:
                if lig1=='ADE':
                    for atom in al_dict.get(lig1)[1].split(';'):
                        atomlist=atomlist+(cmd.get_model('PDB1 and resi '+res_num1+' and name '+atom, 1).get_coord_list())
                else:
                    for atom in al_dict.get(lig1)[0].split(';'):
                        atomlist=atomlist+(cmd.get_model('PDB1 and resi '+res_num1+' and name '+atom, 1).get_coord_list())
                center1=get_center(atomlist)
                
            if center1=='NA':
                    
                    continue
            atomlist=[]                    
                                    
            if lig2 not in al_dict:
                center2=get_center(cmd.get_model('PDB2 and resi '+res_num2, 1).get_coord_list())
            else:
                if lig2=='ADE':
                    for atom in al_dict.get(lig2)[1].split(';'):
                        atomlist=atomlist+(cmd.get_model('PDB2 and resi '+res_num2+' and name '+atom, 1).get_coord_list())
                else:
                    for atom in al_dict.get(lig2)[0].split(';'):
                        atomlist=atomlist+(cmd.get_model('PDB2 and resi '+res_num2+' and name '+atom, 1).get_coord_list())
                center2=get_center(atomlist)
                                 
            if center2=='NA':
                               
                    continue
            #print(center1,center2)
            Dis=math.sqrt((pow((center1[0]-center2[0]),2))+(pow((center1[1]-center2[1]),2))+(pow((center1[2]-center2[2]),2)))
            #print(Dis)
            if Dis>15:
                #print('large distance')
                continue
            #print(x)    
            D= Ql+Tl-(2*x[6])  #was x[1] in all last runs before 4.7.16
            align_out=str(Ql)+'\t'+str(Tl)+'\t'+lig1+'_'+lig2+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+str(x[5])+'\t'+str(x[6])+'\t'+str(Dis)+'\t'+str(D)
            out_file.write(microen1+'\t'+microen2+'\t'+align_out+'\n')	
            #e=time.time()            
            #out_file.write(str(e-s)+'\n')            
            
            
       except:
           err_file.write('\t'.join(line))
           continue
    
    end=time.time()
    print ('Run time is:'+str(end - start)) 
    #out_file.write('Run time is:'+str(end - start)+'/n')     
    out_file.close()
    err_file.close()
    end = time.time()
    cmd.quit()    
    #print ('Run time is:'+str(end - start))            
    
    return # (str(end - start))
	
cmd.extend("pyFunc",pyFunc)
