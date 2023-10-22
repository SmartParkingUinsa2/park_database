from flask import Flask, request, jsonify
import database_server as db

app = Flask(__name__)
db_manager = db.DatabaseManager()

@app.route('/savedata', methods=['POST'])
def save_data():
    try:
        data = request.json  # Menerima data dalam format JSON dari permintaan POST
        
        # Simpan data ke database
        db_manager.save_data(data)
        
        return jsonify(message="Data berhasil disimpan"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/dataparking', methods=['GET'])
def data_parking():
    try:
        area_data = db_manager.get_area()
        if not area_data:
            return jsonify(message="Data area not found"), 404

        images_data = db_manager.get_images()
        if not images_data:
            return jsonify(message="Data images not found"), 404

        parking_data = db_manager.get_parking()
        if not parking_data:
            return jsonify(message="Data parking not found"), 404

        return jsonify(area_data=area_data, images_data=images_data, parking_data=parking_data)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)