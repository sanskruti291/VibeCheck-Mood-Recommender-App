from flask import Flask, request, jsonify
from flask_cors import CORS

from predict_emotions import predict_emotion
from fetch_tracks import fetch_tracks

app = Flask(__name__)
CORS(app)  # Allows requests from your React frontend (localhost or deployed)

# Health check route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok"})


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Please provide text"}), 400

        text = data["text"]

        emotion, confidence = predict_emotion(text)

        tracks = fetch_tracks(emotion)

        return jsonify({
            "emotion": emotion,
            "confidence": confidence,
            "tracks": tracks
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)