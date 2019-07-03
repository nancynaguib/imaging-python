#!/usr/bin/env python
# coding: utf-8

# ## This notebook is used for averaging all radiographs 

# In[ ]:


from PIL import Image
import os, fnmatch
import numpy  as np
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'notebook')
import pylab
import scipy
import pyfits
from os import listdir
from astropy.io import fits


# In[ ]:


rootpath= input('write the path of folders needed to be averaged= (do not include the " ")')


# In[ ]:


savepath=rootpath+'S3_average-all/'
print(rootpath)
print(savepath)


# In[ ]:


if not os.path.exists(savepath):
    os.makedirs(savepath)


# In[ ]:


coll_dir = fnmatch.filter(listdir(rootpath),'*bin_python')
print('the number of radiographs to average=',len(coll_dir))
current_dir=[]


# In[ ]:


# define paths of the folders to be averaged

for k in range(0, len(coll_dir)): # instead of 20 it should be len(coll_dir), number of radiographs
    path= rootpath+coll_dir[k]+'/' # identify the path name (string)
    print(path)
    curr_dir = fnmatch.filter(listdir(path),'*.fits') # read fits files (list) for the first folder in the list of images (one radiograph)


# In[ ]:


for j in range(0, len(curr_dir)): 
        img = np.zeros([512,512],dtype='>f4')
        avg_img = np.zeros([512,512], dtype='>f4')
        for i in range(0, (len(coll_dir)-1)):
            path= rootpath+coll_dir[i]+'/'
#             print(path)
            curr_dir = fnmatch.filter(listdir(path),'*.fits')
            name=path+curr_dir[j]
#             print(name)
            name_dir = name.split(".")
            name_s = name_dir[0].split("/")
            name_sa = name_s[-1].split("_")
            name_save=name_sa[0]+'_'+name_sa[1]
#             print(name_save)
            with fits.open(name) as im:
                data=im[0].data
                img=img+data
        avg_img= np.true_divide(img,(i+1))
        pyfits.writeto(savepath+'S3_avg_img_'+ name_save+'_'+str(f"{j:03}")+'.fits', avg_img)
#         pyfits.writeto(savedir+'S2_avg_img_'+ name_save+'_'+str(f"{j:03}")+'.fits', img)
        print(savepath+'S3_avg_img_'+ name_save+'_'+str(f"{j:03}")+'.fits')

