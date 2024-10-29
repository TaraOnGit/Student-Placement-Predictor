import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Predict:
        def predict_Placement(self,cgpa):


            cgp = np.array(float(cgpa)).reshape(-1,1)
            print('Received CGPA ',cgp)
            df = pd.read_csv('placement.csv')

            X = df.iloc[:,0].values.reshape(-1,1)
            y = df.iloc[:,1].values

            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=2)

            lr = LinearRegression()
            lr.fit(X_train,y_train)

            prediction = lr.predict(cgp)
            print('Placement ', np.round(prediction,2), 'lpa')
            return str(np.round(prediction,2)) + ' Lakhs Per Annum'

#p = Predict()
#p.predict_Placement(8.9)