# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:28:30 2018

@author: hraanan
"""

#%matplotlib inline
import matplotlib.pyplot as plt

import numpy as np

x=[]
y=[]
in_file=open('f:/new_pymol_align_11.5.18/align_filter_NO_ADE_all_with_factor.txt','r')
in_file.readline()

for line in in_file:
    line=line.split('\t')
    try:
        if float(line[15])<100 and float(line[5])<10: 
            x.append(float(line[15]))
            y.append(float(line[5])/float(line[6]))
    except:# IndexError:
        continue
# Estimate the 2D histogram
nbins =50


H, xedges, yedges = np.histogram2d(x,y,bins=nbins)
 
# H needs to be rotated and flipped
H = np.rot90(H)
H = np.flipud(H)
 
# Mask zeros
Hmasked = np.ma.masked_where(H==0,H) # Mask pixels with a value of zero
 
# Plot 2D histogram using pcolor
#xticks = np.arange(0,3,0.4)
xticks = np.arange(0,10,.1)
yticks = np.arange(0,10,1)
fig = plt.figure()
#splt=fig.add_subplot(111)
plt.pcolormesh(xedges,yedges,Hmasked,vmin=0,vmax=60000,)# 
plt.xlabel('Similarity score')
plt.ylabel('RMSD (Å)')
#plt.xticks(xticks)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Counts')
plt.show()