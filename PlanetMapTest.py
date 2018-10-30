# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:49:14 2018

@author: Steven Hill
"""

import scipy.ndimage as nd
import pylab as pl
import numpy as np
import exifread

drive="f:"
path="/Astronomy/Projects/Planets/Mars/Imaging Data/Mapping/"
fn="2018MarsMaster-Bare.png"
f=drive+path+fn
test=nd.imread(f,flatten=True)

pl.imshow(test,"gray")
x=np.zeros([180,360])
x[40:60,100:300]=test[40:60,100:300]
pl.imshow(test[40:60,100:300],"gray")
pl.imshow(x,"gray")
print test.shape

exiftest = open(f, 'rb')
tags = exifread.process_file(exiftest)