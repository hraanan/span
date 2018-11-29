import sys
sys.path.insert(0, 'F:\programs\span')
#sys.path.insert(0, 'F:\programs\span\data')
import center


def cof_color(cof):
    return {
        'CU': '135, 82, 44',
        'FES':'234, 222, 58',
        'Heme':'165, 13, 13',
        'CO':'1, 69, 142',
        'NI':'1, 142, 123',
        'MO':'94, 2, 137',
        'W':'13, 191, 143',
        'FE':'229, 69, 20',
        'MN':'247, 138, 241',
        'V':'51, 34, 50',
        'MG':'67, 178, 33',
        'Ascorbic acid':'210,105,30',
        'Biopterin':'193, 156, 19',
        'Biotin':'205,133,63',
        'Co-A':'244,164,96',
        'Flavin':'41,44,232',
        'Glutathione':'255,228,225',
        'MIO-factor':'112,128,144',
        'Molybdopterin':'176,196,222',
        'NAD':'240,255,240',
        'Tryptophan tryptophylquinone':'230,230,250',
        'lysine tryptophylquinone':'199,21,133',
        "Pyridoxial 5'-phosphate":'30,144,255',
        'Pyrroloquinoline Quinone':'0,0,128',
        'S-adenosylmethionine':'70,130,180',
        'Tetrahydrolic acid':'95,158,160',
        'Thiamine diphosphate':'47,79,79',
        'Quinone':'255,0,255',
        'Chl': '19,193,19'
    }.get(cof,'141, 146, 155')
metal_file=open('F:\programs\span\data\cofactor_metal_content.txt','r')
metal_dict={}
for line in metal_file:
    line=line.split('\t')
    metal_dict[line[0]]=line[1][:-1]
    

#fes=['SF4','F3S','FES']    
in_file=open('microenvironments_metadata_chl_filterd.txt','r')
out_file=open('groups_description_ca_25_rmsd_5_ratio_0.1_md_2_chl_filterd.txt','w')
#in_file.readline()
out_file.write('ID\tgroup size\tcofactors\ttype\tecs\tsingle\tcolor\n')
groups={}
metal=[]
microen_groups={}
microen_cof_dict={}
microen_type_dict={}
prot=[]
for line in in_file:
    line=line.split('\t')
    microen_groups[line[0]]=line[1]
   
#    microen_cof_dict[line[0]]=line[3]
in_file=open('microenvironments_metadata_chl_filterd.txt','r')

for line in in_file:
  
    line=line.split('\t')
    if line[1] not in groups.keys():
        groups[line[1]]=[[line[2]],[line[3]],[line[4]],[line[0]]]
    else:
        
        data=groups.get(line[1])
        if line[2] not in data[0]:
            data[0].append(line[2])
        if line[3] not in data[1]:
            data[1].append(line[3])
        if line[4] not in data[2]:
            data[2].append(line[4])
        data[3].append(line[0])
        groups[line[1]]=[data[0],data[1],data[2],data[3]]
            
for key,value in groups.items():
    prot=[]
    sgl='single'
    for microen in value[3]:
        prot.append(microen[0:4])
        prot=list(set(prot))
        if len(prot)>1:
            sgl=''
            break
    cof_list=[]
    print(value[0])
    for cof in value[0]:
        print(cof)
        if center.is_in_list(cof):
            if center.cof_type(cof) not in cof_list: 
                cof_list.append(center.cof_type(cof))
            
        elif cof in metal_dict.keys():
            #print(cof)
            #print(metal_dict.get(cof))
            if metal_dict.get(cof) not in cof_list:
                cof_list.append(metal_dict.get(cof))
        
    print(cof_list)
    color=cof_color(';'.join(cof_list))
    out_file.write(key+'\t'+str(len(value[3]))+'\t'+';'.join(value[0])+'\t'+';'.join(cof_list)+'\t'+';'.join(value[2])+'\t'+sgl+'\t'+color+'\n')    













#
#for line in in_file:
#    line=line.split('\t')
#    if line[1] not in groups:
#        groups.setdefault(line[1],[]).append(line[2])
#    if line[1] in groups:
#        metal=groups.get(line[1])
#        if line[2] not in metal:
#            metal.append(line[2])
#            metal=sorted(metal)
#groups_size={}
#for group in groups:
#    i=0    
#    sgl='single'
#    prot=[]
#    for key in microen_groups:
#        if microen_groups.get(key)==group:
#            i=i+1
#            prot.append(key[0:4])
#            prot=list(set(prot))
#        if len(prot)>1:
#            sgl=''
#    color=metal_color(';'.join(groups.get(group)))
#    out_file.write(group+'\t'+';'.join(groups.get(group))+'\t'+str(i)+'\t'+sgl+'\t'+color+'\n')
#    #out_file.write(group+'\t'+str(i)+'\t'+sgl+'\t'+color+'\n')
out_file.close()



print('end')