import pandas as pd
import datetime
import numpy as np
from sklearn import linear_model
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib

def tosec(x):
    try:
        a=datetime.datetime.strptime(x,'%H:%M:%S')
        b=a.hour*60*60+a.minute*60+a.second
        return b
    except:
        return 0

def buildmodel():
    ###################################### Preprocessing #################################
    TripData=pd.read_csv('bikeshare/HackBikeShareTO-Trips.csv', delimiter=',', quotechar='|')
    TripData=TripData.dropna(axis=0)
    TripData['Start Date']=pd.to_datetime(TripData['Start Date'])
    TripData['StartSec']=TripData['Start Date'].map(lambda x:x.time().hour*60+x.time().minute)
    TripData['dur']=TripData['Duration'].map(lambda x:tosec(x))
    TripData['End Station ID']=TripData['End Station ID'].astype(int)
    TripData['Start Station ID']=TripData['Start Station ID'].astype(str)
    TripData['End Station ID']=TripData['End Station ID'].astype(str)
    SlicedData=TripData[['StartSec','Start Station ID','End Station ID']].as_matrix()
    keys = ['StartSec','Start Station ID','End Station ID']
    data = [dict(zip(keys, values)) for values in SlicedData[0:]]
    vec = DictVectorizer()
    vecData = vec.fit_transform(data).toarray()
    tar=TripData['dur'].as_matrix()
    
    ###################################### To build the Model #################################
    train=vecData[-200:]
    train_tar=tar[-200:]
    
    
    predModel = linear_model.LinearRegression()
    predModel.fit (train, train_tar)
    
    ###################################### To test the Model #################################
    test=vecData[:200]
    test_tar=tar[:200]
    
    # The coefficients
    print('Coefficients: \n', predModel.coef_)
    
    
    # The mean square error
    print("Residual sum of squares: %.2f" % np.mean((predModel.predict(train) - train_tar) ** 2))
    
    
    #Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % predModel.score(train, train_tar))
    
    ###################################### to save the model and Data #################################
    # to save the model and Data
    _ = joblib.dump(predModel, 'dur_predictor.joblib.pkl', compress=9)
    _ = joblib.dump(vec, 'vectorizer.joblib.pkl', compress=9)
    _ = joblib.dump(data, 'data.joblib.pkl', compress=9)
    _ = joblib.dump(tar, 'tar.joblib.pkl', compress=9)



def predExistingCase(n=600):
    # existing  case
    dur_regr = joblib.load('dur_predictor.joblib.pkl')
    data= joblib.load('data.joblib.pkl')
    tar= joblib.load('tar.joblib.pkl')
    vec= joblib.load('vectorizer.joblib.pkl')
    sam_vec_case = vec.transform(data[n] ).toarray()
    p=dur_regr.predict(sam_vec_case)
    print(data[n] ,'Actual Duration: %i seconds  ||' % tar[n], 'Pridicted Duration:: %.i seconds'% p)
    

def predNewCase(sample_data):
    dur_regr = joblib.load('dur_predictor.joblib.pkl')
    vec= joblib.load('vectorizer.joblib.pkl')
    sam_vec_case = vec.transform(sample_data).toarray()
    p=dur_regr.predict(sam_vec_case)
    print(sample_data,'Pridicted Duration: %.i seconds'% p)

if __name__ == "__main__":
    buildmodel()
    #predExistingCase(602)  # to predict existing  case
    

    
    # new case
    #predNewCase([{'Start Station ID': '7060', 'End Station ID': '7015', 'StartSec': 13}])


