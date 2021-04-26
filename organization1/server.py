from flask import Flask, jsonify, request
from sklearn.datasets.samples_generator import make_blobs
import requests

app = Flask(__name__)

URL_MODEL = "http://model:8080/predict"


@app.route("/predict/<int:id>", methods=["GET"])
def index(id):
    data, _ = make_blobs(n_samples=1, centers=2, n_features=1000, random_state=4)
    payload = list(data[0])
    resp = requests.post(f"{URL_MODEL}/{id}", json=payload)
    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
