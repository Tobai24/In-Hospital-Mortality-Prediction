import pickle
import pandas as pd
from flask import Flask, request, jsonify # type: ignore


with open("save_model.pkl", "rb") as f_in:
    model = pickle.load(f_in)
    
def predict(features):
    preds = model.predict(features)
    return preds


app = Flask("mortality prediction")

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    # Get the JSON data from the request
    data = request.get_json()

    # Convert the list of dictionaries to a DataFrame
    data_df = pd.DataFrame(data)

    # Get the prediction
    pred = predict(data_df)

    # Convert prediction to human-readable output
    result = "alive" if pred >= 0.5 else "dead"

    # Return the result as JSON
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 9696)
    
    