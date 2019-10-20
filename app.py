import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('xgb.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    predictions = model.predict(X_test) 

    # send back to browser
    output = {'results': int(predictions[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)