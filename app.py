from flask import Flask, request
import pickle
from PredictionClass import PredictionClass
import sklearn
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)
app.config.from_mapping(CORS_ORIGINS="https://cc-module-3-taneli.onrender.com/")
with open("./model/prediction_class.pickle", "rb") as f:
  prediction_class: PredictionClass = pickle.load(f)

@app.route("/")
def hello_world():
    return "" \
    "<h1>Hello World!</h1>" \
    "<h3>Version: 4</h3>"

@app.route("/predict", methods=['POST'])
def predict():
     data = request.json
     prediction_text = data['prediction']
     result = prediction_class.predict([prediction_text])
     return {"Verdict": result[0]}