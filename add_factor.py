import os
import time
from multiprocessing import Pool
from itertools import islice

max_rmsd=18.837184906
max_ca=142.0
max_md=4
max_sd=367.0

cores=8

groups_file='f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all.txt'
out_file=open('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_with_factor.txt','w')
head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance'
out_file.write(head+'\tNormalized RMSD\tNormalized CA\tNormalizesd metal distance\tNormalized stractural distance\tFactor\n' )
#groups_file.readline()


def add_factor(line):
    line=line.split("\t") 
    try:
        rmsd=float(line[5])/max_rmsd
       #nrmsd=    float(line[9])/float(line[10])
        
        ca=(max_ca-float(line[6]))/max_ca
        
        md=float(line[9])/max_md
        sd=float(line[10])/max_sd
        factor=rmsd+ca+md+sd
        ave='\t'.join(line)
        if md>15:
            return 'NA'
        x=(ave[:-1]+'\t'+str(rmsd)+'\t'+str(ca)+'\t'+str(md)+'\t'+str(sd)+'\t'+str(factor)+'\n' )
    except:
        return 'NA'
    return x

if __name__ == '__main__':

    
    with open(groups_file, 'r') as infile:
        lines_gen = islice(infile, cores)
        line_list=(list(lines_gen))
        with Pool(cores) as p:
            for line in p.imap_unordered(add_factor,list(line_list)):
                if line !='NA':
                    out_file.write(line)
                #tempfile=open(temp_file,'r')
                #out_file.write(tempfile.read())
                #tempfile.close()
                
out_file.close()
print('end')
        
    









      
        
        
