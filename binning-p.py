#!/usr/bin/env python
# coding: utf-8

# ## This notebook is used to bin the images dataset (fits type) to n images


import os, fnmatch
import numpy  as np
import pylab
import scipy
import pyfits
from os import listdir
from astropy.io import fits


rootpath= input("write the path of folders needed to be binned= (do not include the " ")")
binpath = input("write the path where the folders to be saved= (do not include the " ")")
number = input('write the number of the binning (i.e. 2 or 3 ... so the set will be divided into 2 or 3 groups))')
print(rootpath)


coll_dir_root = fnmatch.filter(listdir(rootpath),'#*')
print(len(coll_dir_root))
print(coll_dir_root)
print((coll_dir_root[185]))


# make 2373 to 2370 images
bin_number=int(number)

for i in range (185, len(coll_dir_root)):
    savepath= binpath+str(coll_dir_root[i])+'_bin_python/'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
        
    datapath= rootpath+str(coll_dir_root[i])+'/Corrected/'
    print(datapath)
    print(savepath)
    current_dir = fnmatch.filter(listdir(datapath),'*.fits')    #to read originial fits
    sorted_dir = sorted(current_dir)
    summed=np.zeros([512,512], dtype='>f4')
    print(type(len(sorted_dir)))
    
    for k in range (0,(len(sorted_dir)-3)):

        unbin=datapath+sorted_dir[k]
        im=fits.open(unbin)
        im_data=im[0].data
        summed=summed+ im_data
        for n in range (0,int(len(sorted_dir)/bin_number)):
            if (k==((n*bin_number)-1)): 
                avg=summed/bin_number
                fitpath= savepath+sorted_dir[k]
                pyfits.writeto(fitpath, avg,clobber= True)
                summed=np.zeros([512,512], dtype='>f4')
