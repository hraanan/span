in_file=open ('align_filter_rmsd_ca_ratio_all_ca_10_ratio_0.1_md_2','r')
out_file=open ('align_filter_rmsd_ca_ratio_all_ca_25_ratio_0.1_md_2','w')
ca=25
rmsd=.1
md=2
in_file.readline()
x=0 
y=0  

for line in in_file:
    x=x+1    
    line=line.split('\t')
    
    try:
       if float(line[11])<rmsd and float(line[6])>ca and float(line[9])<md:
                y=y+1
                join_line= '\t'.join(line)  
                out_file.write(join_line)
    except:# IndexError:
        print('err')        
        continue
print(y,x)
print('end')
out_file.close()