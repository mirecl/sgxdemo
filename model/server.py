from flask import Flask, jsonify, request
from joblib import load
from sklearn.linear_model import LogisticRegression
import requests
import random

app = Flask(__name__)
model = load("model.pkl")

URL_SERVICE_2 = "http://service2:8080/data"
URL_SERVICE_3 = "http://service3:8080/data"


@app.route("/predict/<int:id>", methods=["POST"])
def index(id):
    seed = random.randint(100, 1500)
    data_organization_1 = request.get_json()
    data_organization_2 = requests.get(URL_SERVICE_2)
    data_organization_3 = requests.get(URL_SERVICE_3)
    payload = (
        data_organization_1
        + data_organization_2.json()["data"]
        + data_organization_3.json()["data"]
    )
    vec = sorted(payload)[:100]
    value = model.predict([vec])
    calc = sum(payload[:seed]) / len(payload[:seed])
    return jsonify({"score": float(value + calc)})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
