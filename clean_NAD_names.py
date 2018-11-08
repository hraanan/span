




microen_file=open('f:/new_pymol_align_11.5.18/full_list_of_microenvironments_align_all_no_ADE_2018_with_factor_ca_10_md_3_rmsd_5_with_factor_1.4_chl_synt_filterd.txt','r')
align_file=open ('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_ca_10_md_3_rmsd_5_factor_1.4.txt','r')
microen_out_file=open('microenvironments_list.txt','w')
align_out_file=open('align_1.4.txt','w')


align_out_file.write(align_file.readline())
for line in align_file:
    line=line.split('\t')
    if len(line[0].split('_'))>3 or len(line[1].split('_'))>3:
        continue
    align_out_file.write('\t'.join(line))

for line in microen_file:
    if len(line.split('_'))>3:
        continue
    microen_out_file.write(line)

align_out_file.close()
microen_out_file.close()
print('end')