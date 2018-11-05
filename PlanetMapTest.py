# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:49:14 2018

@author: Steven Hill
"""
import sys
drive='f:'
sys.path.append(drive+'\\Astronomy\Python Play')
sys.path.append(drive+'\\Astronomy\Python Play\Util')
sys.path.append(drive+'\\Astronomy\Python Play\SpectroPhotometry\Spectroscopy')

#import matplotlib.pyplot as pl
#import SysRespLIB as SRL
import ConfigFiles as CF
import GeneralSpecUtils as GSU

import scipy.ndimage as nd
import pylab as pl
import numpy as np
import exifread

drive="f:"
#Target="Mars"
Target="Mars"
path="/Astronomy/Projects/Planets/"+Target+"/Imaging Data/Mapping/"
#fn="2018MarsMaster-Bare.png"



#f=drive+path+fn
MapSetup=CF.PlotSetup("f:/Astronomy/Python Play/PlanetMaps/MapConfig.txt")
MapSetup.loadplotparams(drive,"Mars","Map")

MapSetup.Setup_Map()

if MapSetup.ColorPlane=="Grey":
    test=nd.imread(drive+path+MapSetup.DataFile,flatten=True)
    pl.imshow(test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:],"gray")
elif MapSetup.ColorPlane<>"Grey":
    test=nd.imread(drive+path+MapSetup.DataFile,flatten=False)
    if MapSetup.ColorPlane=="RGB":
        pl.imshow(test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:])
    if MapSetup.ColorPlane=="RED":
        pl.imshow(test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,0],"gray")
    if MapSetup.ColorPlane=="GRN":
        pl.imshow(test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,1],"gray")
    if MapSetup.ColorPlane=="BLU":
        pl.imshow(test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,2],"gray")
    
#pl.imshow(test[0:90,:],"gray")
pl.subplots_adjust(left=0.10, bottom=0.14, right=0.98, top=0.92,
            wspace=None, hspace=None)
pl.savefig(drive+path+"2018MarsMaster-Bare-Output.png",dpi=300)

#x=np.zeros([180,360])
#x[40:60,100:300]=test[40:60,100:300]
#pl.imshow(test[40:60,100:300],"gray")
#pl.imshow(x,"gray")

exiftest = open(f, 'rb')
tags = exifread.process_file(exiftest)