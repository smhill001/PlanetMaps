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
import cartopy.crs as ccrs
import scipy.ndimage as nd
import pylab as pl
import numpy as np
import exifread

drive="f:"
#Target="Mars"
Target="Jupiter"
path="/Astronomy/Projects/Planets/"+Target+"/Imaging Data/Mapping/"
#fn="2018MarsMaster-Bare.png"

#f=drive+path+fn
MapSetup=CF.PlotSetup("f:/Astronomy/Python Play/PlanetMaps/MapConfig.txt")
MapSetup.loadplotparams(drive,"Jupiter-2013-RGB","Map")

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

fig=pl.figure(figsize=(6., 3.), dpi=150, facecolor="white")
ax = pl.axes(projection=ccrs.PlateCarree())
ax.imshow(test, "gray",origin='upper', transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90])

pl.show()

lon = np.linspace(-180, 180, 360)
lat = np.linspace(90, -90, 180)
#lon2d, lat2d = np.meshgrid(lon, lat)

test_crs = ccrs.PlateCarree()
test_extent=[-180.,180.,-90.,90]


fig1=pl.figure(figsize=(6., 3.), dpi=150, facecolor="white")
ax1 = pl.axes(projection=ccrs.SouthPolarStereo())
#ax1.stock_img()
#ax1.imshow(test, "gray",origin='upper', transform=ccrs.Mollweide(), extent=[-180, 180, -90, 90])
#ax1.set_global()
#ax1.coastlines()
ax1.set_extent([-180, 180, -90, 20], crs=ccrs.PlateCarree())
ax1.gridlines(crs=test_crs)
#ax1.xticks(np.arange(0,360,30),np.mod(np.arange(540,179,-30),360))

ax1.imshow(test,transform=test_crs,extent=test_extent,origin="upper",cmap="gray")  
pl.show()

#x=np.zeros([180,360])
#x[40:60,100:300]=test[40:60,100:300]
#pl.imshow(test[40:60,100:300],"gray")
#pl.imshow(x,"gray")

#exiftest = open(f, 'rb')
#tags = exifread.process_file(exiftest)