import pickle
import pandas as pd
import logging

def load_saved_model():
    filename = 'final_rf_model.sav'
    model = pickle.load(open(filename, 'rb'))
    test_df = pd.read_csv('testData.csv')
    X_test = test_df.drop(['Class'], axis =1)
    y_test = test_df['Class']
    score = model.score(X_test,y_test)* 100
    logging.basicConfig(level=logging.INFO)
    logging.info("The test accuracy of the model: {0:.2f}%".format(score))
    return model

def predict_fraud(nparray,model):
    prediction = model.predict(nparray)
    return prediction