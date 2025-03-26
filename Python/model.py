import numpy as np
from flask import Flask, abort, jsonify, request, render_template
import pickle
import json

rfc = pickle.load(open("anemiaTrained.pkl", "rb"))

app = Flask(__name__)
@app.route("/home")
def my_form():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def make_predict():
    data = request.get_json(force=True)
    predict_anemia = [data['RBC'],data['HB'],data['MCV'], data['MCH'], data['MCHC'], data['RDW']] 
    predict_anemia = np.array(predict_anemia).reshape(1,-1)
    y_hat = rfc.predict(predict_anemia)
    output = {'Condition': str(y_hat[0])}
    print(output)
    results = output

    return jsonify(results=results)


if __name__ == '__main__':
     app.run(port = 7000, debug = True)