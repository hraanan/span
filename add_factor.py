import sys

max_rmsd=18.837184906
max_ca=142.0
max_md=4
max_sd=367.0


in_file_name=sys.argv[1]
groups_file=open(in_file_name,'r')
out_file=open(in_file_name+'_out.txt','w')
head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance'
out_file.write(head+'\tNormalized RMSD\tNormalized CA\tNormalizesd metal distance\tNormalized stractural distance\tFactor\n' )
groups_file.readline()


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
    t=0
    lines=[]
    for line in groups_file:
        i=add_factor(line)
        if i!='NA':
            out_file.write(i)
                
out_file.close()
print('end')
        
    









      
        
        
