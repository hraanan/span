in_file=open('f:/span/align_all_ADE_rename_2016.txt','r')   
in_file.readline()
out_file=open('f:/span/align_all_no_ADE_2016.txt','w')
ade_file=open('f:/span/align_ADE_2016.txt','w')


head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n'
out_file.write(head)
ade_file.write(head)
i=0
for line in in_file:
#    i=i+1
#    if i>1000:
#        break
    line=line.split('\t')
    cof1=line[0].split('_')[0]
    cof2=line[1].split('_')[0]
    cof1=cof1.split('.')[1]
    cof2=cof2.split('.')[1]
    
    line[0]='_'.join(line[0].split('_')[:3])
    line[1]='_'.join(line[1].split('_')[:3])      
    if cof1=='ADE' or cof2=='ADE':
        ade_file.write('\t'.join(line))
        continue
    out_file.write('\t'.join(line))
ade_file.close()
out_file.close()
print('end')