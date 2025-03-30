from flask import Flask
import pickle
from PredictionClass import PredictionClass
import sklearn

app = Flask(__name__)

with open("./model/prediction_class.pickle", "rb") as f:
  prediction_class: PredictionClass = pickle.load(f)

@app.route("/")
def hello_world():
    return "" \
    "<h1>Hello World!</h1>" \
    "<h3>Version: 4</h3>"

@app.route("/test")
def test():
    prediction = ["This is bad"]
    result = prediction_class.predict(prediction)
    return result

if __name__ == '__main__':
     app.run(host="0.0.0.0", port="8080", debug=False)