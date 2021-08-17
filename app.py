# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 06:59:39 2021

@author: Gautam
"""


import numpy as np
from flask import Flask
import pickle
from flask import request, jsonify, render_template

app = Flask(__name__)


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 2)
    loaded_model = pickle.load(open("Fraud_Detection.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
    if int(result) == 1:
        prediction = 'Given transaction is Fraud'
    else:
        prediction = 'Given transaction is NO Fraud'
    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug = True,
        port=8050,
        host='127.0.0.1'
    )