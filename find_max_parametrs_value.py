
groups_file=open('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all.txt',"r")
#groups_file.readline()
max_rmsd=0
max_ca=0
max_md=0
max_sd=0
print(groups_file.readline())

for line in groups_file:
    
    try:
        
        line=line.split("\t")
       # if float(line[9])/float(line[10])>max_rmsd:max_rmsd=float(line[9])/float(line[10]) :
        if float(line[5])>max_rmsd:max_rmsd=float(line[5])
        if float(line[6])>max_ca:max_ca=float(line[6]) 
        if float(line[9])>max_md:max_md=float(line[9])
        if float(line[10][:-1])>max_sd:max_sd=float(line[10][:-1])     
    except:# ValueError:
        print(line)
        continue

#Organics
#max_rmsd=18.2348499298
#max_ca=140.0
#max_md=3.99999918577
#max_sd=268.0  

#Chl
#max_rmsd=18.2959671021
#max_ca=105.0
#max_md=3.99999918577
#max_sd=193.0


print (max_rmsd,max_ca,max_md,max_sd)
#Metals
#max_rmsd=17.7648162842
#max_ca=138.0
#max_md=3.99999918577
#max_sd=404.0     
#groups_file.close()



#ChlNewCenter
#max_rmsd=18.249666214
#max_ca=123.0
#max_md=4
#max_sd=253.0


#OrganicNewCenter
#max_rmsd=18.837184906
#max_ca=142.0
#max_md=4
#max_sd=385.0

print('end')
        