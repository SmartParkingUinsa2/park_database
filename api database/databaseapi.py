from flask import Flask, request, jsonify
import databasesv as db
import os

app = Flask(__name__)

image_directory = "gambar"

db_manager = db.DatabaseManager()

@app.route("/insert_area", methods=["POST"])
def insert_area():
    try:
        data = request.get_json()
        area_name = data["area_name"]
        db_manager.insert_area(area_name)
        return jsonify({"message": "Area inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/insert_images", methods=["POST"])
def insert_images():
    try:
        # Menerima file gambar dari permintaan POST
        if 'image' in request.files:
            image = request.files['image']
            
            # Pastikan direktori "gambar" ada
            if not os.path.exists(image_directory):
                os.makedirs(image_directory)
            
            # Simpan file gambar ke direktori "gambar"
            image_path = os.path.join(image_directory, image.filename)
            image.save(image_path)
            
            # Simpan path gambar ke database
            db_manager.insert_images(image_path)
            
            return jsonify({"message": "Image inserted successfully"})
        else:
            return jsonify({"error": "No image file found in the request"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/insert_parking_data", methods=["POST"])
def insert_parking_data():
    try:
        data = request.get_json()
        # Parse the JSON data and insert into the database using db_manager
        db_manager.insert_parking_data(data["id_area"], data["id_images"], data["hari"], data["jam"],
                                      data["jumlah_spd"], data["jumlah_spdm"], data["jumlah_mobil"])
        return jsonify({"message": "Parking data inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
