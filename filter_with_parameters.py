in_file=open ('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_with_factor.txt','r')
out_file=open ('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_with_factor_ca_10_md_3_rmsd_5.txt','w')
ca=10
rmsd=5
md=3
in_file.readline()
x=0 
y=0  

for line in in_file:
    x=x+1    
    line=line.split('\t')
    
    try:
       if float(line[5])<rmsd and float(line[6])>ca and float(line[9])<md:
                y=y+1
                join_line= '\t'.join(line)  
                out_file.write(join_line)
    except:# IndexError:
        print('err')        
        continue
print(y,x)
print('end')
out_file.close()