




in_file=open('f:/new_pymol_align_11.5.18/microenvironments_list.txt','r')
out_file=open('f:/new_pymol_align_11.5.18/nonredundant_microenvironments_list.txt','w')
nonredundant_file=open('f:/programs/span/data/cullpdb_pc90_res3.0_R0.3_d181024_chains_90%_10.24.18.txt','r')

#in_file.readline()
#out_file.write('ID\tgroup\tcofactor\tmetal\tcofactor_group\tec\thead\tmolecule\torganism_scientific\tno rank\tsuperkingdom\tphylum\tclass\torder\tfamily\tgenus\torganism_taxid\tname\tchains\tresolution\tstructure_method\tkeywords\tjournal_reference\trelease_date\n')
nonredundant_file.readline()
nonredundant=[]
for line in nonredundant_file:
    line=line.split('\t')
    nonredundant.append(line[0].lower()+'_'+line[1])
for line in in_file:
    line=line.split('\t')
    microen=line[0].split('_')
    prot_chain=microen[0][:4]+'_'+microen[1]
    if prot_chain in nonredundant:
        out_file.write('\t'.join(line))