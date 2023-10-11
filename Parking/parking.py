import json
import sqlite3


class ParkingAppBackend:
    def __init__(self):
        self.conn = sqlite3.connect("parking.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open(
            "parking.sql", "r"
        ) as sqlfile:  # Pastikan nama file dan pathnya sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # Simpan perubahan ke database

    def save_area(self, id_area, area):
        try:
            # Mengonversi list deskripsi menjadi format JSON
            # area_list = [area]
            # area_json = json.dumps(area_list)
            self.cursor.execute("INSERT INTO area (id_area, area) VALUES (?)", (id_area, area))
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan data area:", str(e))
            return False

    def save_images(self, id_images, path_images):
        try:
            self.cursor.execute(
                "INSERT INTO images (id_images, path_images) VALUES (?, ?)", (id_images, path_images)
            )
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error saat menyimpan data images:", str(e))
            return False
        
    def save_parking(self, id_parking, id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil):
        try:
            self.cursor.execute(
                "INSERT INTO parking (id_parking, id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    id_parking,
                    id_area,
                    id_images,
                    hari,
                    jam,
                    jumlah_spd,
                    jumlah_spdm,
                    jumlah_mobil
                ),
            )
            self.conn.commit()  # Simpan perubahan ke database
            return True
        except Exception as e:
            print("Error:", str(e))
            return False
