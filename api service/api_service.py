from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Gantilah URL dengan URL API machine learning Anda
ML_API_URL = "https://your-ml-api-url.com/"

# Gantilah URL dengan URL API database Anda yang menerima data melalui POST
DB_API_URL = "https://2djncpz1-8080.asse.devtunnels.ms/"

# Endpoint untuk melakukan prediksi menggunakan API machine learning
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Mengambil data dari permintaan POST

        # Kirim data ke API machine learning
        ml_response = requests.post(ML_API_URL, json=data)

        if ml_response.status_code == 200:
            prediction = ml_response.json()
        else:
            return jsonify({"error": "Failed to get prediction from ML API"}), 500

        # Kirim data hasil prediksi ke API database
        db_response = requests.post(DB_API_URL, json={"data": data, "prediction": prediction})

        if db_response.status_code == 200:
            return jsonify({"prediction": prediction, "database_response": db_response.json()}), 200
        else:
            return jsonify({"error": "Failed to save prediction to database"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)