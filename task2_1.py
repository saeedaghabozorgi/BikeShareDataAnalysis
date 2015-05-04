import pandas as pd

if __name__ == "__main__":
    # to load data
    TripData=pd.read_csv('bikeshare/HackBikeShareTO-Trips.csv', delimiter=',', quotechar='|')
    # To slice data
    data=TripData.ix[:,['Trip ID','Start Station Name','End Station Name']]
    # To clean data
    data=data.dropna(axis=0)
    # To Group by data
    result=data['Trip ID'].groupby([data['Start Station Name'], data['End Station Name']]).count()
    result.reset_index()
    result.sort(0,False)
    print(result[0:10])