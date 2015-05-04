import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
from random import randint
data=[]


data=pd.read_csv('bikeshare/distances_output.csv', delimiter=',', quotechar='|', header=None)

a=data[3]
lat=a[a>0].tolist()

b=data[4]
lon=b[b<0].tolist()

c=pd.read_csv('bikeshare/HackBikeShareTO-CycleApp.csv', delimiter=',', quotechar='|')


x=[randint(0,11522086) for p in range(0,500)]
c=c.iloc[x]
pyplot.plot(c['Longitude'],c['Latitude'],'-')
pyplot.plot(lon,lat,'ro')
pyplot.show()



