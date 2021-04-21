from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def index():
    return jsonify({"body": request.get_json()})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
