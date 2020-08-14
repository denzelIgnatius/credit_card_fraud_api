import flask
from flask import request, jsonify
from Transaction_obj import Transaction
from predict_fraud import load_saved_model, predict_fraud

#init app
app = flask.Flask(__name__)
model = load_saved_model()

@app.route('/test', methods = ['GET'])
def get_test_msg():
    return jsonify("Test message")

@app.route('/predict', methods = ['POST'])
def predictApi():
    time = request.json['Time']
    v1 = request.json['V1']
    v2 = request.json['V2']
    v3 = request.json['V3']
    v4 = request.json['V4']
    v5 = request.json['V5']
    v6 = request.json['V6']
    v7 = request.json['V7']
    v8 = request.json['V8']
    v9 = request.json['V9']
    v10 = request.json['V10']
    v11 = request.json['V11']
    v12 = request.json['V12']
    v13 = request.json['V13']
    v14 = request.json['V14']
    v15 = request.json['V15']
    v16 = request.json['V16']
    v17 = request.json['V17']
    v18 = request.json['V18']
    v19 = request.json['V19']
    v20 = request.json['V20']
    v21 = request.json['V21']
    v22 = request.json['V22']
    v23 = request.json['V23']
    v24 = request.json['V24']
    v25 = request.json['V25']
    v26 = request.json['V26']
    v27 = request.json['V27']
    v28 = request.json['V28']
    amount = request.json['Amount']
    trans = Transaction(time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, 
        v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount)
    prediction = predict_fraud(trans.get_transaction_array(),model).tolist()[0]
    return jsonify(fraud = prediction)
    

#run app
if __name__ == '__main__':
    app.run(debug = True)


