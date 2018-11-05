# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:01:28 2018

This creates a list for pairwise alignment 


@author: hraanan
"""

#rootdir ='F:/microfolds_8_2018/all/' # folder of the pdb original filesdownladed form the pdb

import time
import sys
import os
in_file_name=sys.argv[1]
out_file_name='/mnt/f/align_out_'+in_file_name.split('.')[1]+'.txt'

out_file=open(out_file_name,'w')
print(os.curdir())
out_file.write(out_file_name)
#time.sleep(10)
out_file.close()
print('end')
        
        