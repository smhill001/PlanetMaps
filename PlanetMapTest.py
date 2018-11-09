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
    
    #import matplotlib.pyplot as pl
    #import SysRespLIB as SRL
    import ConfigFiles as CF
    import GeneralSpecUtils as GSU
    import cartopy.crs as ccrs
    import scipy.ndimage as nd
    import pylab as pl
    import numpy as np
    import exifread
    
    drive="f:"
    #Target="Mars"
    path="/Astronomy/Projects/Planets/"+Target+"/Imaging Data/Mapping/"
    #fn="2018MarsMaster-Bare.png"
    
    #f=drive+path+fn
    MapSetup=CF.PlotSetup("f:/Astronomy/Python Play/PlanetMaps/MapConfig.txt")
    MapSetup.loadplotparams(drive,PlotID,"Map")
    
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
    pl.savefig(drive+path+PlotID+".png",dpi=300)
    
    ###########################################################Start of CartoPy
    #ax.gridliner(x,)
    #ax.xtick_labels(-np.linspace(-180,180,13))
    
    MapSetup.Setup_CaratoPy_Map()
    
    test_crs = ccrs.PlateCarree()
    test_extent=[-180,180,int(MapSetup.Y0),int(MapSetup.Y1)]
    print "BEFORE CONDITIONAL"
    if len(test.shape)>2: 
        test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:,:]
    else:
        test_patch=test[90-int(MapSetup.Y1):90-int(MapSetup.Y0),:]
        
    print "test_extent=",test_extent
    pl.imshow(test_patch, "gray",origin='upper', transform=ccrs.PlateCarree(), extent=test_extent)
    
    pl.subplots_adjust(left=0.10, bottom=0.14, right=0.98, top=0.92,
                wspace=None, hspace=None)
    
    lon = np.linspace(-180, 180, 360)
    lat = np.linspace(90, -90, 180)
    #lon2d, lat2d = np.meshgrid(lon, lat)
    
    test_extent=[-180.,180.,-90.,90]
    
    fig1=pl.figure(figsize=(6., 3.), dpi=150, facecolor="white")
    ax1 = pl.axes(projection=ccrs.PlateCarree())
    ax1.set_extent([-180, 180, -90, 20], crs=ccrs.PlateCarree())
    ax1.gridlines(crs=test_crs,linewidth=0.2)
    ax1.set_xticks(np.arange(-180,179,30), minor=False, crs=ccrs.PlateCarree())
    ax1.imshow(test,transform=test_crs,extent=test_extent,origin="upper",cmap="gray")  
    
    
    #x=np.zeros([180,360])
    #x[40:60,100:300]=test[40:60,100:300]
    #pl.imshow(test[40:60,100:300],"gray")
    #pl.imshow(x,"gray")
    
    #exiftest = open(f, 'rb')
    #tags = exifread.process_file(exiftest)
    return 0