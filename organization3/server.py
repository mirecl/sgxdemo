from flask import Flask, jsonify, request
from sklearn.datasets.samples_generator import make_blobs

app = Flask(__name__)


@app.route("/data", methods=["GET"])
def index():
    data, _ = make_blobs(n_samples=1, centers=2, n_features=1000, random_state=4)
    resp = list(data[0])
    return jsonify({"data": resp})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
