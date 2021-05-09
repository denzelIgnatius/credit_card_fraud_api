import pickle
import pandas as pd
import logging

def load_saved_model():
    filename = 'final_rf_model.sav'
    model = pickle.load(open(filename, 'rb'))
    if model == None:
        raise Exception("Error: loading model failed")
    test_df = pd.read_csv('test data/testData.csv')
    if len(test_df) == 0:
        raise Exception("Error: loading test data failed")
    X_test = test_df.drop(['Class'], axis =1)
    y_test = test_df['Class']
    score = model.score(X_test,y_test)* 100
    logging.basicConfig(level=logging.INFO)
    logging.info("The test accuracy of the model: {0:.2f}%".format(score))
    return model, X_test.columns

def predict_fraud(nparray,model):
    if len(nparray) == 0:
        raise Exception("Error: Missing data for prediction")
    if model == None:
        raise Exception("Error: Model not initialized")
    prediction = model.predict(nparray)
    return prediction
