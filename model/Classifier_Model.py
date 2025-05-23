import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV


"""main classifier model"""
def Heart_Disease_Classification_Model(X_train, X_test, y_train, y_test):

    

    model=LogisticRegression(C= 0.23357214690901212,solver='liblinear')

    model.fit(X_train,y_train)
   

    with open('model/_model.pkl', 'wb') as file:
        pickle.dump(model, file)


if __name__=='__main__':

    df=pd.read_csv('dataset/heart-disease.csv')
    X=df.drop('target',axis=1)
    y=df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    Heart_Disease_Classification_Model( X_train, X_test, y_train, y_test)

    

