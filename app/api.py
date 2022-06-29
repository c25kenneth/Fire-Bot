from flask import Flask, request, make_response
import pickle
import pandas as pd

pickle_in = open('app/model.pickle', 'rb')
linear = pickle.load(pickle_in)
df = pd.read_csv("forestfires.csv")
df = df.drop(["month", "day", "FFMC", "DMC", "DC", "ISI"], 1)
app = Flask(__name__)

@app.route("/predict/<X>/<y>/<temp>/<RH>/<wind>/<rain>/", methods=["GET"])
def predictFire(X, y, temp, RH, wind, rain):
    if request.method == "GET":
        prediction = linear.predict([ [X, y, temp, RH, wind, rain] ])
        return {"prediction": str(prediction)}

@app.route("/getdataset", methods=['GET'])
def getData():
    if request.method == "GET": 
        return {"data": str(df.head())}

if __name__ == '__main__':
    app.run(debug=True)