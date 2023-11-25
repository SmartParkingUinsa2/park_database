from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/ambildata', methods=['GET'])
def ambil_data():
    conn = sqlite3.connect('db_desktop_dummy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM parkir')
    rows = cursor.fetchall()
    conn.close()

    parkir_data = []
    for row in rows:
        parkir_data.append({
            'id': row[0],
            'tahun': row[1],
            'bulan': row[2],
            'tanggal': row[3],
            'hari': row[4],
            'jam': row[5],
            'area': row[6],
            'jenis_kendaraan': row[7],
            'jumlah_kendaraan': row[8]
        })

    return jsonify({'parkir_data': parkir_data})

@app.route('/store', methods=['POST'])
def store_data():
    # Get the data from the request
    data = request.get_json()

    # Connect to the database
    conn = sqlite3.connect('db_desktop_dummy.db')
    cursor = conn.cursor()

    # Insert data into the "parkir" table
    tahun = data['tahun']
    bulan = data['bulan']
    tanggal = data['tanggal']
    hari = data['hari']
    jam = data['jam']
    area = data['area']
    jeke = data['jenis_kendaraan']  # Adjust this based on the JSON structure sent
    juke = data['jumlah_kendaraan']  # Adjust this based on the JSON structure sent
    cursor.execute("INSERT INTO parkir (tahun, bulan, tanggal, hari, jam, area, jeke, juke) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (tahun, bulan, tanggal, hari, jam, area, jeke, juke))

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()

    return 'Data stored in the database.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
