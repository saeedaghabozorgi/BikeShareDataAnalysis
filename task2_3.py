from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import numpy as np

# to calculate the spatiol distance between two points
def spatiaDis(lat1,lon1,lat2,lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

# to calculate distances according to altitude and longtit
def dist(x):
    return spatiaDis(x[3], x[4], x[6], x[7])

if __name__ == "__main__":
    data=pd.read_csv('bikeshare/distances_output.csv', delimiter=',', quotechar='|', header=None)
    data['dirDis']=data.apply(dist,axis=1)
    
    data['dif']=data[2]-data['dirDis']
    data=data.sort(columns='dif', ascending=False)
    print(data[2:5][[0,1,2,'dirDis','dif']])
