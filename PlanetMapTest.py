# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:49:14 2018

@author: Steven Hill
"""

def PlanetMapTest(Target,PlotID):
    import sys
    drive='f:'
    sys.path.append(drive+'\\Astronomy\Python Play')
    sys.path.append(drive+'\\Astronomy\Python Play\Util')
    sys.path.append(drive+'\\Astronomy\Python Play\SpectroPhotometry\Spectroscopy')
    import matplotlib.path as mpath

    import ConfigFiles as CF
    import PlotUtils as PU
    import cartopy.crs as ccrs
    import scipy.ndimage as nd
    import pylab as pl
    import numpy as np
    import exifread
    
    drive="f:"
    path="/Astronomy/Projects/Planets/"+Target+"/Imaging Data/Mapping/"
    
    MapSetup=PU.PlotSetup("f:/Astronomy/Python Play/PlanetMaps/MapConfig.txt")
    MapSetup.loadplotparams(drive,PlotID,"Map")
    fig=pl.figure(figsize=(6.0, 6.0), dpi=150, facecolor="white")
    MapSetup.Setup_CaratoPy_Map("PC",2,1,1)
    if MapSetup.ColorPlane=="Grey":
        test=nd.imread(drive+path+MapSetup.DataFile,flatten=True)
    elif MapSetup.ColorPlane<>"Grey":
        test=nd.imread(drive+path+MapSetup.DataFile,flatten=False)
    
    test_crs = ccrs.PlateCarree()
    test_extent=[-180,180,int(MapSetup.Y0),int(MapSetup.Y1)]
    print "BEFORE CONDITIONAL"
    print test.shape
    if len(test.shape)>2:
        print MapSetup.ColorPlane
        if MapSetup.ColorPlane=="RGB":
            test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,:]
        if MapSetup.ColorPlane=="RED":
            test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,0]
        if MapSetup.ColorPlane=="GRN":
            test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,1]
        if MapSetup.ColorPlane=="BLU":
            test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,2]      
    else:
        if MapSetup.ColorPlane=="Grey":
            test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:]
        
    print "test_extent=",test_extent
    pl.imshow(test_patch, "gray",origin='upper', transform=ccrs.PlateCarree(), extent=test_extent)
    
    pl.subplots_adjust(left=0.08, bottom=0.14, right=0.98, top=0.92,
                wspace=None, hspace=None)
    ###########################################################################
   
    #test_extent=[-180.,180.,-90.,90]
    
    #fig1=pl.figure(figsize=(6., 3.), dpi=150, facecolor="white")

    MapSetup.Setup_CaratoPy_Map("NP",2,2,3)
    pl.imshow(test_patch,transform=test_crs,extent=test_extent,origin="upper",cmap="gray")  

    MapSetup.Setup_CaratoPy_Map("SP",2,2,4)  
    pl.imshow(test_patch,transform=test_crs,extent=test_extent,origin="upper",cmap="gray")  

    pl.savefig(drive+path+PlotID+".png",dpi=300)
    
    #x=np.zeros([180,360])
    #x[40:60,100:300]=test[40:60,100:300]
    #pl.imshow(test[40:60,100:300],"gray")
    #pl.imshow(x,"gray")
    
    #exiftest = open(f, 'rb')
    #tags = exifread.process_file(exiftest)
    
    return 0