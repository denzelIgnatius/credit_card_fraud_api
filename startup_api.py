import flask, json
from flask import request, jsonify, render_template
from predict_fraud import load_saved_model, predict_fraud
from jsonHandler import createResponseObj, parseJsonData
import numpy as np

#init app
app = flask.Flask(__name__)
model, colnnames = load_saved_model()

@app.route('/', methods = ['GET'])
def homePage():
    return render_template('index.html')

@app.route('/single_prediction', methods = ['POST'])
def predictSingleApi():
    try:
        result, col = validataDatapoint(request.json)
        if not result:
            return jsonify("Error: Missing value for " + col)
        data = parseJsonData([request.json],colnnames)
        prediction = predict_fraud(np.array(data).reshape(1,-1),model).tolist()
        return jsonify(createResponseObj(prediction))
    except Exception as error:
        return jsonify(str(error.args))

@app.route('/multiple_prediction', methods = ['POST'])
def predictMultipleApi():
    try:
        result, col = validataDataset(request.json['dataset'])
        if not result:
            return jsonify("Error: Missing value for " + col)
        data = parseJsonData(request.json['dataset'],colnnames)
        prediction = predict_fraud(np.array(data), model).tolist()
        return jsonify(createResponseObj(prediction))
    except Exception as error:
        return jsonify(str(error.args))

def validataDatapoint(jsonkeys):
    keys = jsonkeys.keys()
    for col in colnnames:
        if col not in keys:
            return False, col
    return True, None

def validataDataset(jsonList):
    for jsonObj in jsonList:
        result, col = validataDatapoint(jsonObj)
        if not result:
            return False, col
    return True, None

#run app
if __name__ == '__main__':
    app.run(threaded=True, port=5000)


