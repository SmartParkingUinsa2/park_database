import mysql.connector

class DatabaseManager:
    def __init__(self):
        # Konfigurasi koneksi ke database MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Ganti dengan nama pengguna Anda
            password="",  # Ganti dengan kata sandi Anda (jika ada)
            database="parking"  # Ganti dengan nama database yang Anda gunakan
        )
        self.cursor = self.connection.cursor()

        
    def save_data(self, data):
        placeholders = ', '.join(['%s'] * len(data))
        query = """
        INSERT INTO images(id_area, area)
        VALUES(%s, %s)
        """
        self.cursor.execute(query, data)
        self.connection.commit()

    def get_area(self):
        try:
            query = "SELECT * FROM area"
            self.cursor.execute(query)

            area_data = self.cursor.fetchall()
            return area_data
        except Exception as e:
            print("Error:", e)
            return []

    def save_data1(self, data):
        placeholders = ', '.join(['%s'] * len(data))
        query = """
        INSERT INTO images(id_images, path_images)
        VALUES(%s, %s)
        """
        self.cursor.execute(query, data)
        self.connection.commit()
    
    def get_images(self):
        try:
            query = "SELECT * FROM images"
            self.cursor.execute(query)

            images_data = self.cursor.fetchall()
            return images_data
        except Exception as e:
            print("Error:", e)
            return []
        
    def save_data2(self, data):
        query = """
           INSERT INTO parking(id_parking, id_area, id_images, hari, jam, jumlah_spd, jumlah_spdm, jumlah_mobil)
           VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, data)
        self.connection.commit()

    def get_parking(self):
        try:
            query = "SELECT * FROM parking"
            self.cursor.execute(query)

            parking_data = self.cursor.fetchall()
            return parking_data
        except Exception as e:
            print("Error:", e)
            return []

    def close_connection(self):
        # Menutup koneksi ke database MySQL
        self.connection.close()