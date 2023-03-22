import json
from flask import Flask, request, jsonify
from model import Model

app = Flask(__name__)
model = Model()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data["text"]
    prediction = model.recognize_entities(text)
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
