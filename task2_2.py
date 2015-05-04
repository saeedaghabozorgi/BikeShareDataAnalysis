import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

if __name__ == "__main__":

    ##########   To count the frequency of trips
    t=pd.read_csv('bikeshare/HackBikeShareTO-Trips.csv', delimiter=',', quotechar='|')
    t=t.dropna(axis=0)
    t['Start Date']=pd.to_datetime(t['Start Date'])
    t['dt']=t['Start Date'].map(lambda x:x.date())
    result=t['Trip ID'].groupby([t['dt']]).count()
    
    
    ######### to convert date time into date
    w=pd.read_csv('bikeshare/HackBikeShareTO-Weather.csv', delimiter=',', quotechar='|')
    w=w.dropna(axis=0)   
    w['Date']=pd.to_datetime(w['Date'])
    w['dt']=w['Date'].map(lambda x:x.date())
    w.index=w['dt']
    
    ##### Join tables
    f=pd.concat([w,result], axis=1, join='inner')
    
    
    ##### To plot the freq against date
    f['Trip ID']=f['Trip ID']/50
    plt.plot(f['dt'],f[['Trip ID', 'Mean_Temperature_C']])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.ylabel('Temp & TripFreq/50')
    plt.xlabel('Date')
    plt.show()
    
    
    print(numpy.corrcoef(f['Trip ID'],f['Mean_Temperature_C']))
    #plt.figure(1)
    #plt.subplot(121)
    #plt.plot(f[[ 'Mean_Temperature_C']])
    #plt.ylabel('Mean Temp')
    #plt.subplot(122)
    #plt.plot(f[['Trip ID']])
    #plt.ylabel('Trip Freq')
    #plt.xlabel('Date')
    #plt.show()


    
